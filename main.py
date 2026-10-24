try:
    user1 = float(input('Первое значение: '))
    user2 = float(input('Второе значение: '))
except ZeroDivisionError:
    print('Нельзя делить на ноль')
except:
    print('Должны быть только цифры/числа')
else:
    number = user1 / user2
    print(f'{number:.2f}')
finally:
    print('\nПрограмма завершена')
