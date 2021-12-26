import os


def find(f):
    i = f.readline()
    chislo = i.split()[0]
    return chislo


def actions(number, quantity=0, amount=0, composition=1):
    for i in range(len(number)):
        quantity += 1
        amount += int(number[i])
        composition *= int(number[i])
    return quantity, amount, composition


def output(f1, number, quantity, amount, composition):
    f1.write(f'Число: {number}\n')
    f1.write(f'Количество цифр: {quantity}\n')
    f1.write(f'Сумма цифр: {amount}\n')
    f1.write(f'Произведение цифр: {composition}\n')


def main():
    if os.path.exists("input.txt"):
        f = open("input.txt", "r")
        number = find(f)
        quantity, ammount, composition = actions(number)
        f1 = open("output.txt", "w")
        output(f1, number, quantity, ammount, composition)
        f.close()
        f1.close()
    else:
        print('Файл с входными данными не обнаружен')


if __name__ == "__main__":
    main()
