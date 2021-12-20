f = open("inputasd")
i = f.readline()
x = 0
for r in range(len(i)):
    print(i[r], ord(i[r]))
    x += ord(i[r])
print(x)