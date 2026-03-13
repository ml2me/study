import random
import numpy as np

RANDOM_STATE = 42

def gv_spliter(text2tok):  #  tokenizer
    return text2tok.split()


random.seed(RANDOM_STATE)
def init_random_vec(tok_list2vec, vec_dimension):
    token_vectors = {}
    for token in tok_list2vec:
        token_vectors[token] = np.array([random.uniform(0, 1) for _ in range(vec_dimension)])
    return token_vectors

def train(data: str):
    """
    return: w2v_dict: dict
            - key: string (word)
            - value: np.array (embedding)
    """
    return init_random_vec(gv_spliter(data), 2)
	
gv_clean_text = 'эта функция часто используется в nlp обработке естественного языка для предварительной подготовки текста перед анализом или векторизацией'

p = train(gv_clean_text)

for k,v in p.items():
    print(f"{k}: {v}")