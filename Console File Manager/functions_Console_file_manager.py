import os
import shutil
from math import *
from use_functions import my_score
from victory import victorina

# print('1. создать папку')
# print('2.удалить (файл/папку) ')
# print('3. копировать (файл/папку)')
# print('4.просмотр содержимого рабочей директории ')
# print('5. посмотреть только папки')
# print('6. посмотреть только файлы')
# print('7. просмотр информации об операционной системе')
# print('8. создатель программы')
# print('9. играть в викторину')
# print('10. мой банковский счет')
# print('11. cмена рабочей директории ')
# print('12. переименовать файл')
# print('13. выход')

#создание файла
def create_a_folder(name_f):
    k = 0
    not_error = 0
    yes_error = 0
    try:
        not_error = 1
        os.mkdir(name_f)
    except FileExistsError:
        yes_error = 1
        print('Папка с таким именем уже существует')
    finally:
        k = not_error+yes_error
    return k



def delete_file(name_file):
    #удаление файла в текущей директории
    k = 0
    not_error = 0
    yes_error = 0
    try:
        not_error = 1
        os.rmdir(name_file)
    except FileNotFoundError:
        yes_error = 1
        print('Файла с таким именем не существует')
    finally:
        k = not_error+yes_error
    return k


def copy_file():
    # копирование файла
    name_file_copy = input("Введите имя копируемого файла: ")
    name_file_new = input("Введите имя нового файла: ")
    shutil.copy(name_file_copy, name_file_new)

def review_directory():
    # просмотр содержимого рабочей директории
    print(os.listdir())

def review_a_folders_directory():
    for root, dirs, files in os.walk(os.getcwd()):
        return dirs

def review_files_directory():
    for root, dirs, files in os.walk(os.getcwd()):
        return files
def save_info_directory_in_listdirTxt():
    # сохранение информации о содержимом рабочей директории
    with open('listdir.txt', 'w') as f:
        f.write(f'files:{review_files_directory()}\n')
        f.write(f'dirs:{review_a_folders_directory()}\n')


def info_os():
    """
    информация об операционной системе
    """
    try:
        print(os.uname())
    except AttributeError:
        print(os.name)
        print(os.environ)

def program_author(): # информация об авторе программы
    author_program = 'Соколов Александр Валерьевич'
    return author_program

def new_directory():# открываем новую директорию
    os.chdir(input('Укажите новую директорию: '))

def file_rename():#переименовываем файл
    name_file_rename = input("Введите имя файла Для переименования: ")
    new_name_file = input("Введите новое имя файла: ")
    os.rename(name_file_rename, new_name_file)

def one_pi():
    one = pi/pi
    return one