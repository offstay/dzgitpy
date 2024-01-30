import os
import shutil
import subprocess

def create_file(file_name):
    with open(file_name, 'w') as f:
        pass

def create_folder(folder_name):
    os.makedirs(folder_name)

def delete_file(file_name):
    os.remove(file_name)

def delete_folder(folder_name):
    shutil.rmtree(folder_name)

def move(source, destination):
    shutil.move(source, destination)

def copy(source, destination):
    shutil.copy2(source, destination)

def git_init():
    subprocess.run(['git', 'init'])

def git_add(file_or_folder):
    subprocess.run(['git', 'add', file_or_folder])

def git_commit(message):
    subprocess.run(['git', 'commit', '-m', message])

def git_status():
    subprocess.run(['git', 'status'])

def main():
    while True:
        print("\n1. Создать файл")
        print("2. Создать папку")
        print("3. Удалить файл")
        print("4. Удалить папку")
        print("5. Переместить файл/папку")
        print("6. Копировать файл/папку")
        print("7. Инициализировать Git репозиторий")
        print("8. Добавить файл/папку в Git")
        print("9. Сделать коммит в Git")
        print("10. Показать статус Git")
        print("0. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            file_name = input("Введите имя файла: ")
            create_file(file_name)
        elif choice == '2':
            folder_name = input("Введите имя папки: ")
            create_folder(folder_name)
        elif choice == '3':
            file_name = input("Введите имя файла: ")
            delete_file(file_name)
        elif choice == '4':
            folder_name = input("Введите имя папки: ")
            delete_folder(folder_name)
        elif choice == '5':
            source = input("Введите путь к исходному файлу/папке: ")
            destination = input("Введите путь к целевой папке: ")
            move(source, destination)
        elif choice == '6':
            source = input("Введите путь к исходному файлу/папке: ")
            destination = input("Введите путь к целевой папке: ")
            copy(source, destination)
        elif choice == '7':
            git_init()
        elif choice == '8':
            file_or_folder = input("Введите путь к файлу/папке для добавления в Git: ")
            git_add(file_or_folder)
        elif choice == '9':
            commit_message = input("Введите сообщение для коммита: ")
            git_commit(commit_message)
        elif choice == '10':
            git_status()
        elif choice == '0':
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
