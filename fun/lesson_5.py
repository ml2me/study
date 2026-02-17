import os

# 1. Подготовим среду для эксперимента
# Создадим файл, чтобы он точно существовал
with open('data_file.txt', 'w') as f:
    f.write('some data')
# Создадим папку, чтобы она тоже точно существовала
os.makedirs('data_folder', exist_ok=True)


# 2. Теперь начнем проверки
path_to_file = 'data_file.txt'
path_to_folder = 'data_folder'
non_existent_path = 'ghost_file.txt'

print(f"--- Начинаю проверку ---")

# Проверка №1: Существующий файл
if os.path.exists(path_to_file):
    print(f"✅ Путь '{path_to_file}' СУЩЕСТВУЕТ.")
else:
    print(f"❌ Путь '{path_to_file}' НЕ существует.")

# Проверка №2: Существующая папка
if os.path.exists(path_to_folder):
    print(f"✅ Путь '{path_to_folder}' СУЩЕСТВУЕТ.")
else:
    print(f"❌ Путь '{path_to_folder}' НЕ существует.")

# Проверка №3: Несуществующий путь
if os.path.exists(non_existent_path):
    print(f"✅ Путь '{non_existent_path}' СУЩЕСТВУЕТ.")
else:
    print(f"❌ Путь '{non_existent_path}' НЕ существует.")

# 3. Не забудем убрать за собой (хорошая практика)
os.remove(path_to_file)
os.rmdir(path_to_folder)