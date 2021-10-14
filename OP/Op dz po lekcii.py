# Первый способ
a = int(input())
b = int(input())
a = a + b
b = a - b
a = a - b
print('a =',a,'b =',b)

# Второй способ
a = int(input())
b = int(input())
c = 0
c = a
a = b
b = c
print('a =', a,'b =',b)
