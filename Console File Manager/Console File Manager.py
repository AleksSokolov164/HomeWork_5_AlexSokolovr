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
        name_file = input('Введите название название папки')
        os.mkdir(name_file)
    elif choice == '2':
        name_file = input('Введите название название папки')
        os.rmdir(name_file)
    elif choice == '3':
        name_file_copy = input("Введите имя копируемого файла: ")
        name_file_new = input("Введите имя нового файла: ")
        shutil.copy(name_file_copy, name_file_new)
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':
        for root, dirs, files in os.walk(os.getcwd()):
            print(dirs)
            break

    elif choice == '6':
        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
        print(onlyfiles)

        # from os import walk
        # f = []
        # for (dirpath, dirnames, filenames) in walk(os.getcwd()):
        #     f.extend(filenames)
        #     break
        # print(f)

        #import glob
        #print(os.getcwd())
        #print(glob.glob("os.getcwd()/*.py"))
    elif choice == '7':
        try:
            print(os.uname())
        except AttributeError:
            print(os.name)
            print(os.environ)
    elif choice == '8':
        print('Соколов Александр Валерьевич')
    elif choice == '9':
        victorina()
    elif choice == '10':
        my_score()
    elif choice == '11':
        os.chdir(input('Укажите новую директорию: '))
    elif choice == '12':
        name_file_rename = input("Введите имя файла Для переименования: ")
        new_name_file = input("Введите новое имя файла: ")
        os.rename(name_file_rename, new_name_file)
    elif choice == '13':
        break
    else:
        print('Неверный пункт меню')