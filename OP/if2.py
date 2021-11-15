x = int(input('Введите номер месяца'))
if x == 12 or x == 1 or x == 2:
    print('Сейчас Зима')
elif x == 3 or x == 4 or x == 5:
    print('Сейчас Весна')
elif x == 6 or x == 7 or x == 8:
    print('Сейчас Лето')
else:
    print('Сейчас Осень')