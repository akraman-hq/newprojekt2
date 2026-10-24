try:
    user1 = float(input('Первое значение: '))
    user2 = float(input('Второе значение: '))
    number = user1 / user2
    print(number)
except:
    print('Должны быть только цифры/числа')