try:
    user1 = float(input('Первое значение: '))
    user2 = float(input('Второе значение: '))
    number = user1 / user2
except ZeroDivisionError:
    print('Нельзя делить на ноль')
except:
    print('Должны быть только цифры/числа')
else:
    print(f'{number:.2f}')
finally:
    print('\nПрограмма завершена')

