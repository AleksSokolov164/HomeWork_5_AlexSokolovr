"""
В проекте создать новый модуль test_python.py
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
 Чем больше тестов на каждую функцию - тем лучше
"""
from math import *
from functions_Console_file_manager import *




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