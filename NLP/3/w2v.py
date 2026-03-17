import numpy as np
import re
import string
from collections import defaultdict, Counter
import random

# Параметры модели
vector_dimension = 30 
context_size = 9
number_of_epochs = 5 
learning_rate = 0.01

class Word2VecEmbedder:
    def __init__(self, vector_dim=vector_dimension, context=context_size, epochs=number_of_epochs, lr=learning_rate):
        self.vector_dim = vector_dim
        self.context_size = context
        self.epochs = epochs
        self.lr = lr
        self.word2idx = {}
        self.idx2word = []
        self.embeddings = None
        self.vocab_size = 0

    def build_vocab(self, corpus_text: str):
        """Построение словаря на основе корпуса текста (одной строки)"""
        word_counts = Counter()
        cleaned = corpus_text
        words = cleaned.split()
        word_counts.update(words)

        # Сортируем слова по частоте
        self.idx2word = ['<UNK>'] + [word for word, _ in word_counts.most_common()]
        self.word2idx = {word: idx for idx, word in enumerate(self.idx2word)}
        self.vocab_size = len(self.idx2word)

        # Инициализация эмбеддингов случайными значениями
        self.embeddings = np.random.randn(self.vocab_size, self.vector_dim) * 0.01

    def generate_training_pairs(self, corpus_text: str):
        """Генерация пар (центр, контекст) для обучения из одного текстового корпуса"""
        pairs = []
        cleaned = corpus_text
        words = cleaned.split()
        word_indices = [self.word2idx.get(w, 0) for w in words]  # 0 - индекс для <UNK>

        for i, center_idx in enumerate(word_indices):
            # Определяем границы контекстного окна
            start = max(0, i - self.context_size)
            end = min(len(word_indices), i + self.context_size + 1)

            # Добавляем контекстные слова
            for j in range(start, end):
                if i != j:  # Исключаем само слово
                    pairs.append((center_idx, word_indices[j]))

        return pairs

    def pre_train(self, texts: str):
        """Обучение модели с помощью Negative Sampling, принимая корпус как одну строку"""
        self.build_vocab(texts)
        training_pairs = self.generate_training_pairs(texts)

        # Вспомогательные матрицы для обучения
        W1 = self.embeddings  # Матрица входных эмбеддингов
        W2 = np.random.randn(self.vocab_size, self.vector_dim) * 0.01  # Матрица выходных эмбеддингов

        for epoch in range(self.epochs):
            random.shuffle(training_pairs)
            total_loss = 0

            # Проверяем, что training_pairs не пуст, чтобы избежать ZeroDivisionError
            if not training_pairs:
                print(f"Epoch {epoch+1}/{self.epochs}, Loss: N/A (No training pairs generated)")
                continue

            for center_idx, context_idx in training_pairs:
                # --- Обучение на позитивном примере (основное обучение) ---
                # Получаем векторы для центрального слова и позитивного контекста
                center_vec = W1[center_idx]
                context_vec = W2[context_idx]

                # Вычисляем скор и вероятность для позитивного примера (целевое значение: 1)
                score = np.dot(center_vec, context_vec)
                prob = 1 / (1 + np.exp(-score))  # Сигмоида
                loss = -np.log(prob + 1e-8) # Лосс для позитивного примера
                total_loss += loss

                # Вычисляем градиенты для позитивного примера
                grad = prob - 1  # (predicted_prob - target_value), target_value = 1
                grad_center = grad * context_vec
                grad_context = grad * center_vec

                # Обновляем веса на основе позитивного примера
                W1[center_idx] -= self.lr * grad_center
                W2[context_idx] -= self.lr * grad_context

                # --- Обучение на негативных примерах (Negative Sampling) ---
                num_negative = 5 # Количество негативных примеров
                for _ in range(num_negative):
                    neg_idx = np.random.randint(self.vocab_size) # Выбираем случайный негативный индекс
                    # Убедимся, что негативный пример не совпадает с позитивным или центральным словом
                    if neg_idx == context_idx or neg_idx == center_idx:
                        continue

                    neg_vec = W2[neg_idx]
                    score_neg = np.dot(center_vec, neg_vec)
                    prob_neg = 1 / (1 + np.exp(-score_neg)) # Вероятность, что это позитивный (но мы хотим 0)
                    loss_neg = -np.log(1 - prob_neg + 1e-8) # Лосс для негативного примера (целевое значение: 0)
                    total_loss += loss_neg

                    # Вычисляем градиенты для негативного примера
                    grad_neg = prob_neg # (predicted_prob - target_value), target_value = 0
                    grad_center_neg = grad_neg * neg_vec
                    grad_neg_vec = grad_neg * center_vec

                    # Обновляем веса на основе негативного примера
                    W1[center_idx] -= self.lr * grad_center_neg
                    W2[neg_idx] -= self.lr * grad_neg_vec

            print(f"Epoch {epoch+1}/{self.epochs}, Loss: {total_loss/len(training_pairs):.4f}")

        # Сохраняем обученные эмбеддинги
        self.embeddings = W1
        
        # ВОЗВРАЩАЕМ словарь эмбеддингов
        return self.get_embedding_dict()

    def get_word_embedding(self, word):
        """Получение эмбеддинга для слова"""
        idx = self.word2idx.get(word, 0)
        return self.embeddings[idx]

    def get_embedding_dict(self):
        """Возвращает словарь {слово: эмбеддинг}"""
        return {word: self.embeddings[idx] for word, idx in self.word2idx.items()}


def train(data: str):
    """
    return: w2v_dict: dict
            - key: string (word)
            - value: np.array (embedding)
    """
    embedder = Word2VecEmbedder()
    return embedder.pre_train(data)
