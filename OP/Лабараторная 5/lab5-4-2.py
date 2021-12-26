def entry():
    a = float(input('1'))
    b = float(input('2'))
    c = float(input('3'))
    return a, b, c


def extraction(a, b, c):
    global x2, x1
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        k = 2
    elif discriminant == 0:
        x1 = (-b + discriminant ** 0.5) / 2 * a
        x2 = x1
        k = 1
    else:
        k = 0
    return x1, x2, k


def main():
    a, b, c = entry()
    print("Уравнение:\n" + f"({a})*x^2+({b})*x+({c})=0")
    x1, x2, k = extraction(a, b, c)
    print(f"Количество корней: {k}")
    if x1 != 0:
        if x1 > x2:
            print(x2)
            print(x1)
        else:
            print(x1)
            print(x2)


x1 = 0
x2 = 0
if __name__ == "__main__":
    main()

