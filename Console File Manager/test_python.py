"""
В проекте создать новый модуль test_python.py
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
 Чем больше тестов на каждую функцию - тем лучше
"""
from math import *
from functions_Console_file_manager import *

def test_sorted():
    assert sorted([5, 2, 3, 1, 4,1]) == [1,1, 2, 3, 4, 5]
    assert sorted([5, 2, 3, 1, 4, 1],reverse=True) == [5, 4, 3, 2, 1, 1]
    assert sorted('adaretfdsqq') == ['a', 'a', 'd', 'd', 'e', 'f', 'q', 'q', 'r', 's', 't']
    assert sorted({2: 'D', 1: 'B', 3: 'B', 4: 'E', 5: 'A'}) == [1, 2, 3, 4, 5]
    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]
    assert sorted(student_tuples, key=lambda student: student[2]) == [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]  # сортируем по возрасту


def test_filter():
    a = [-1, 0, 1, 0, 0, 1, 0, -1]
    assert list(filter(None, a)) == [-1, 1, 1, -1]
    strong = 'a1b2c3d4e6f7i8t9'
    assert list(filter(set, strong)) == ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '6', 'f', '7', 'i', '8', 't', '9']
    s = ['a', '', 'c', 'd', ' ']
    assert list(filter(None, s)) == ['a', 'c', 'd', ' ']

def test_map():
    number = [-2,-1,0,1,2]
    strong = ['1', 'a', 'b', '+c', 'dddd']
    boolean = [True, False]
    def f (x):
        return x*2
    assert list(map(f, number)) == [-4,-2,0,2,4]
    assert  list(map(f, strong)) == ['11', 'aa', 'bb', '+c+c', 'dddddddd']
    assert list(map(f,boolean)) == [ 2, 0 ]
    assert list(map(f, [5,4])) == [10,8]


def test_one_pi():
    assert one_pi() == 1

def test_trunc():
    assert pi//3 == 1
    assert pi/pi == 1
    assert pi//1 ==3
    assert trunc(pi) == 3

def test_sqrt():
    for i,j in [[4,2],[9,3],[16,4],[25,5]]:
        assert sqrt(i) == j
    for i in range(100):
        assert sqrt(i*i) == i

def test_pow():
    for i in range(100):
        assert pow(i,2) == i**2

def test_hypot():
    for i in range(100):
        assert hypot(i, 2) == sqrt(i*i + 2 * 2)
        assert hypot(4,i) == (4 * 4 + i * i)**0.5