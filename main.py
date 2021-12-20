f = open("informatica/inputasd")
i = f.readline()
x = 0
for r in range(len(i)):
    print(i[r], ord(i[r]))
    x += ord(i[r])
print(x)
x = str(x ** 2)
print(x)
if len(x) % 2 == 0:
    s = int(x[len(x)//2 - 1]+x[len(x)//2])
    print(x[len(x)//2 - 1]+x[len(x)//2])
else:
    s = int(x[len(x)//2])
    print(x[len(x)//2])
print(s%7)
