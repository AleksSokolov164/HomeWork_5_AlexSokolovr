"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета personal account
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное менюп

2. покупка purchase
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок purchase history
 

выводим историю покупок пользователя (название purchase name
 
 и сумму purchase price)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import datetime

def add_separators(f): # декоратор
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('*' * 100)
        result = f(*args, **kwargs)
        # поведение после вызова
        # print('*' * 100)
        return result
    # возвращается функция inner с новым поведением
    return inner

@add_separators
def print_decor(strk): # итоговая функция вывода с использованием декоратора
    print(strk)


def date_today():
    return datetime.datetime.today().strftime("%d-%m-%Y") # дата совершения операции

def time_today():
    return  datetime.datetime.today().strftime("%H.%M.%S")  # время совершения операции

def separator(simbol, count):  # функция вывода разделительной строки из знаков simbol  в кол-ве count
    k = simbol * count
    return (k)


def my_score():
    import os
    import pickle

    try:
        with open('orders_pickle.data', 'rb') as f:
            purchase_history = pickle.load(f)
    except FileNotFoundError:
        purchase_history = []
        print('История операций отсутствует')

    try:
        n_operatin = purchase_history[-1][0]  # номер операции со счетом
    except IndexError:
        n_operatin = 0
        # operatin = 'Сумма на счете'  # описание операции со счетом
        debit = float(0)  # приход по счету пользователя
        credit = float(0)  # расход по счету пользователя
    try:
        with open('total_save.txt', 'r') as f:
            # Читаем сумму на счете из файла
            total = float(f.readline())
            total_debit = float(f.readline())# итог по дебету
            total_credit = float(f.readline())# итог по кредиту
    except FileNotFoundError:
        total = 0
        total_debit = 0  # итог по дебету
        total_credit = 0  # итог по кредиту
    print( f' Сумма на счете: {total}')

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. снятие наличных')
        print('5. выход')
        choice = input('Выберите пункт меню ')
        if choice == '1':
            n_operatin = n_operatin + 1  # номер операции со счетом
            operatin = 'зачисление '  # описание операции со счетом
            debit = float(input('Введите сумму пополнения счета: '))  # приход по счету пользователя
            credit = float(0)  # расход по счету пользователя
            total = total + debit  # сумма на счету пользователя
            purchase_history.append([n_operatin, operatin, debit, credit, total,date_today(),time_today()])
            total_debit = total_debit+debit

        elif choice == '2':
            credit = float(input('Введите цену покупки: '))  # расход по счету пользователя
            if credit > total:
                print('У Вас недостаточно средств на счете') # проверка на платежеспособность
            else:
                n_operatin = n_operatin + 1  # номер операции со счетом
                debit = float(0)  # приход по счету пользователя
                operatin = input('Введите название покупки: ')  # описание операции со счетом
                total = total - credit  # сумма на счету пользователя
                purchase_history.append([n_operatin, operatin, debit, credit, total,date_today(),time_today()])
                total_credit = total_credit+credit

        elif choice == '3':
            width_n_operatin = 5  # ширина столбца - номер операции со счетом
            width_operatin = 25   # ширина столбца -описание операции со счетом
            width_debit = 15  # ширина столбца -приход по счету пользователя
            width_credit = 15  # ширина столбца -расход по счету пользователя
            width_total = 10  # ширина столбца -сумма на счету пользователя
            print_decor('N    операция                    приход           расход           итог         дата       время ')

            for i in purchase_history:
                tail_width_n_operatin = ' '*(width_n_operatin-len(str(i[0]))) # выравнивание по сроке - номер операции со счетом
                tail_width_operatin = ' '*(width_operatin- len(i[1]))  # выравнивание по сроке -описание операции со счетом
                tail_width_debit = ' '*(width_debit-len(str(i[2])))  # выравнивание по сроке -приход по счету пользователя
                tail_width_credit = ' '*(width_credit-len(str(i[3])))  # выравнивание по сроке -расход по счету пользователя
                tail_width_total = ' '*(width_total-len(str(i[4])))  # выравнивание по сроке -сумма на счету пользователя
                print_decor(f'{i[0]} {tail_width_n_operatin} {i[1]} {tail_width_operatin} {i[2]} {tail_width_debit} '
                       f'{i[3]} {tail_width_credit} {i[4]} {tail_width_total}  {i[5]} {i[6]} ')

            print_decor(f'       ИТОГО                      {total_debit}              {total_credit}              {total} ')

        elif choice == '4':
            credit = float(input('Введите сумму для снятия: '))  # расход по счету пользователя
            if credit > total:
                print('У Вас недостаточно средств на счете') # проверка на платежеспособность
            else:
                debit = float(0)  # приход по счету пользователя
                operatin = 'выдача наличных '  # описание операции со счетом
                total = total - credit  # сумма на счету пользователя
                n_operatin = n_operatin + 1  # номер операции со счетом
                purchase_history.append([n_operatin, operatin, debit, credit, total,date_today(),time_today()])
                total_credit = total_credit+credit

        elif choice == '5':
            with open('total_save.txt', 'w') as f:
                #Записываем в файл сумму. дебет и кредит
                f.writelines([f'{str(total)}\n', f'{str(total_debit)}\n', f'{str(total_credit)}\n'])
            with open('orders_pickle.data', 'wb') as f:
                # записываем в файл историю операций
                pickle.dump(purchase_history, f)
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    print('Проверка фукции')
    my_score()