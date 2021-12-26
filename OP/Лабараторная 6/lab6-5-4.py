import datetime
import os


def find(f):
    r = f.readline()
    r = r.replace(' ', '')
    r = r.replace('\n', '')
    i = f.readline()
    x, y = i.split()
    return r, x, y


def actions(r, x, y, k=1):
    for i in range(x - r, x + r):
        for j in range(y - 1, y + r):
            if ((x ** 2) + (y ** 2)) ** 0.5 <= r:
                k += 1
    return k


def output(f1, quantity, time):
    f1.write(f'{time}\n')
    f1.write(f'{quantity}\n')
    execution_time = datetime.datetime.now() - time
    f1.write(f'{execution_time}\n')


def main():
    if os.path.exists("input.txt"):
        f = open("input.txt", "r")
        r, x, y = find(f)
        r, x, y = int(r), int(x), int(y)
        quantity = actions(r, x, y)
        f1 = open("output.txt", "w")
        output(f1, quantity, start_time)
        f.close()
        f1.close()

    else:
        print('Файл с входными данными не обнаружен')


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
