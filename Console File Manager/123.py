answer = 'ДА'
while answer=="ДА":
    print('1')
    answer = str(input("Желаете повторить ещё раз? (да\нет)")).upper()
    while answer != 'ДА' or answer != 'НЕТ' :
        list_answer =['ДА', 'НЕТ' ]
        my_answer = "Хорошо!" if answer in list_answer else "Введите 'ДА' или 'НЕТ' пожалуйста"
        print(my_answer)
        answer = str(input("Желаете повторить ещё раз? (да\нет)")).upper()