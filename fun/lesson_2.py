import os
import sys

print(f"Мой скрипт находится в папке: {os.getcwd()}")

print(f"Я использую версию Python: {sys.version}")
print("------------------------------------")
#  system_name = os.name
print(f"Имя моей операционной системы: {os.name}")

print("------------------------------------")
if os.name == 'nt': # Для Windows
    username_variable = 'USERNAME'
    home_variable = 'USERPROFILE'
else: # Для macOS и Linux
    username_variable = 'USER'
    home_variable = 'HOME'

username = os.environ[username_variable]
home_directory = os.environ[home_variable]

print(f"Имя пользователя в системе: {username}")
print(f"Путь к домашней директории: {home_directory}")

# 2. Также мы можем получить доступ к знаменитой переменной PATH
system_path = os.environ['PATH']
print(f"\nПеременная PATH: {system_path}")

print("------------------------------------")
# Пытаемся получить секретный ключ. Если его нет, используем 'default_key'
api_key = os.environ.get('SECRET_API_KEY', 'default_key_12345')
print(f"Используемый API ключ: {api_key}")

# Пытаемся получить режим отладки. Если переменная не задана, вернется None
debug_mode = os.environ.get('DEBUG_MODE')

if debug_mode is not None:
    print(f"Режим отладки включен со значением: {debug_mode}")
else:
    print("Режим отладки выключен.")

print("------------------------------------")
