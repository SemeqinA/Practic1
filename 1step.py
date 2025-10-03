import os

def main():
    while True:
        # Приглашение к вводу
        user = os.getenv('USER', 'user')
        host = os.getenv('COMPUTERNAME', 'host')
        dir_name = os.path.basename(os.getcwd())
        prompt = f"{user}@{host}:{dir_name}$ "
        
        # Ввод команды
        cmd = input(prompt).strip()
        
        if not cmd:
            continue
            
        # Раскрытие переменных окружения
        cmd = os.path.expandvars(cmd)
        
        # Разбивка на команду и аргументы
        parts = cmd.split()
        command = parts[0]
        args = parts[1:]
        
        # Выполнение команд
        if command == "exit":
            print("Выход")
            break
        elif command == "ls":
            print(f"ls: {args}")
        elif command == "cd":
            print(f"cd: {args}")
        else:
            print(f"Ошибка: команда '{command}' не найдена")

if __name__ == "__main__":
    main()