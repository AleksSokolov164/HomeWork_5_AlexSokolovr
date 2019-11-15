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
def create_a_folder():
   # создание папки в текущей директори
    name_file = input('Введите название название папки')
    os.mkdir(name_file)

def delete_file():
    #удаление файла в текщей директории
    name_file = input('Введите название название папки')
    os.rmdir(name_file)

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
        print(dirs)
        break

def review_files_directory():
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
    print(onlyfiles)

def info_os():
    try:
        print(os.uname())
    except AttributeError:
        print(os.name)
        print(os.environ)

def program_author():
    print('Соколов Александр Валерьевич')

def new_directory():
    os.chdir(input('Укажите новую директорию: '))

def file_rename():
    name_file_rename = input("Введите имя файла Для переименования: ")
    new_name_file = input("Введите новое имя файла: ")
    os.rename(name_file_rename, new_name_file)

def one_pi():
    one = pi/pi
    return one