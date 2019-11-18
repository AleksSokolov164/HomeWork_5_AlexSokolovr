"""
1. Создать новый проект ""Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку
- удалить (файл/папку)
- копировать (файл/папку)
- просмотр содержимого рабочей директории
- посмотреть только папки
- посмотреть только файлы
- просмотр информации об операционной системе
- создатель программы
- играть в викторину
- мой банковский счет
- cмена рабочей директории (*необязательный пункт)
- выход
так же можно добавить любой дополнительный функционал по желанию

Описание пунктов:
- создать папку
после выбора пользователь вводит название папки, создаем её в рабочей директории
- удалить (файл/папку)
после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть
- копировать (файл/папку)
после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем
- просмотр содержимого рабочей директории
вывод всех объектов в рабочей папке
- посмотреть только папки
вывод только папок которые находятся в рабочей папке
- посмотреть только файлы
вывод только файлов которые находятся в рабочей папке
- просмотр информации об операционной системе
вывести информацию об операционной системе (можно использовать пример из 1-го урока)
- создатель программы
вывод информации о создателе программы
- играть в викторину
запуск игры викторина из предыдущего дз
- мой банковский счет
запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать)
- смена рабочей директории (*необязательный пункт)
усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь. Меняем рабочую директорию на ту что ввели и работаем уже в ней
- выход
выход из программы
- дополнительно - переименование файла
"""
import os
import shutil
from use_functions import my_score
from victory import victorina
from functions_Console_file_manager import *

while True:
    print('1. создать папку')
    print('2.удалить (файл/папку) ')
    print('3. копировать (файл/папку)')
    print('4.просмотр содержимого рабочей директории ')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. cмена рабочей директории ')
    print('12. переименовать файл')
    print('13. выход')
    choice = input('Выберите пункт меню')
    if choice == '1':
        create_a_folder()
    elif choice == '2':
        delete_file()
    elif choice == '3':
        copy_file()
    elif choice == '4':
        review_directory()
    elif choice == '5':
        review_a_folders_directory()

    elif choice == '6':
        review_files_directory()
    elif choice == '7':
        info_os()
    elif choice == '8':
        print(program_author())
    elif choice == '9':
        victorina()
    elif choice == '10':
        my_score()
    elif choice == '11':
        new_directory()
    elif choice == '12':
        file_rename()
    elif choice == '13':
        break
    else:
        print('Неверный пункт меню')