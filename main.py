import subprocess
import sys
from datetime import datetime

def speeds_up_git_routine(text_4_commit='routine'):
    try:
        command_1 = subprocess.run(['git', 'pull'], capture_output=True, text=True)
        
        if command_1.returncode == 0:
            print('Git pull выполнен успешно')
            print(command_1.stdout)
        else:
            print(f'Git pull завершился с ошибкой (код {command_1.returncode})')
            print(command_1.stderr)
        
        command_2 = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)

        if command_2.returncode == 0:
            print('Git add выполнен успешно')
            print(command_2.stdout)
        else:
            print(f'Git add завершился с ошибкой (код {command_2.returncode})')
            print(command_2.stderr)

        command_3 = subprocess.run(['git', 'commit', '-m', text_4_commit], capture_output=True, text=True)

        if command_3.returncode == 0:
            print('Git commit выполнен успешно')
            print(command_3.stdout)
        else:
            print(f'Git commit завершился с ошибкой (код {command_3.returncode})')
            print(command_3.stderr)

    except subprocess.SubprocessError as e:
        print(f'Ошибка при выполнении команды: {e}')
        sys.exit(1)

if len(sys.argv) == 1:
    text_from_user = f'routine {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' 
else:
    text_from_user = ' '.join(sys.argv[1:])

speeds_up_git_routine(text_from_user)
