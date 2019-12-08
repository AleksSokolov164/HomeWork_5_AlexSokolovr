import os


# 1. Функция это объект
def f():
    pass


a = f


# print(a)


# 2. функцию можно передавать параметром в другую функцию
def ff(param):
    pass


ff(f)


# Функция декоратор
# f - исходная фукнция
def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('*' * 10)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('*' * 10)
        return result

    # возвращается функция inner с новым поведением
    return inner


# 3. Зачем нужны декораторы
@add_separators
def hello():
    # что то сделать перед вызовом функции
    print('hello' * 10)

    # что то сделать после вызова функции


@add_separators  # аналогично other = add_separators(other)
def other():
    return 'other'


@add_separators
def my_sum(a, b):
    return a + b

@add_separators
def yes(strk):
    print(strk)

if __name__ == '__main__':
    hello()

    result = other()
    print(result)

    new_list_dir = add_separators(os.listdir)

    print(new_list_dir())

    result = my_sum(2, 4)
    print(result)

    yes("kjh")

