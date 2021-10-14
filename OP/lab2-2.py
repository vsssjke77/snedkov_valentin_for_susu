# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9

print(type(number))   # Вывод типа переменной number

float_number = 9.0

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов

i = 'Привет'

z = 4

t = "}"

float_number = int(float_number)

print("i", type(i))

print("z", type(z))

print("t", type(t))

print("float_number", type(float_number))

# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.

print(int(z))

print(float(z))

print(str(z))

z = 'sa'

s = bool(z)

print(s)
