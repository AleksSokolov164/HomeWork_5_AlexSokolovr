'''
создать модуль test_filemanager.py для тестирования функций консольного файлового менеджера
В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина

(Дополнительно*) так же попробовать написать тесты для ""грязных"" функций, например копирования файла/папки, ...
'''
from functions_Console_file_manager import *
from victory import victorina

# тестируем функцию выводящую данные об авторе программы
def test_program_author():
    assert program_author() == 'Соколов Александр Валерьевич'

#тестируем функцию создания файла
def test_create_a_folder():
    name_file = "file_for_testing"
    assert create_a_folder(name_file) == 1

#тестируем функцию удаления  файла
def test_delete_file():
    name_file = "file_for_testing"
    assert delete_file(name_file) == 1

