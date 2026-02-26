import sys

print("--- 'План поиска' модулей (sys.path) ---")

# Просто перебираем список и выводим каждый пункт плана
for index, folder in enumerate(sys.path):
    print(f"Шаг {index}: Проверить папку '{folder}'")