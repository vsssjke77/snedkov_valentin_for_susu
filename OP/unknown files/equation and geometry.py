import math
variant = (27 + 4) % 4 + 1
print(variant)

#equation

x = int(input("Введите x"))
y = (x + (x + (x) ** 0.5) ** 0.5) ** 0.5
print(y)

#geometry
a = int(input("Введите угол при основании"))
q = (a*math.pi)/180
r = int(input("Введите величину радиуса"))
S = (4 * (r ** 2)) / math.sin(q)
print(S)
