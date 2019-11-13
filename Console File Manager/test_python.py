"""
В проекте создать новый модуль test_python.py
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
 Чем больше тестов на каждую функцию - тем лучше
"""
from math import *

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