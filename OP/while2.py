y = int(input())
x = int(input())
r = y
d = 0
if y > 0 and x > 0:
    while r >= x:
        r = r - x
        d = d + 1
    print(str(y) + "%" + str(x) + "=" + str(r))
    print(str(y) + "//" + str(x) + "=" + str(d))
elif y < 0 and x < 0:  # только для отрицательных чисел
    while r <= x:
        r = r - x
        d = d + 1
    print(str(y) + "%" + str(x) + "=" + str(r))
    print(str(y) + "//" + str(x) + "=" + str(d))