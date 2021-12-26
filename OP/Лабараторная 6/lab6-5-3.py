import os


def find(f):
    i = f.readline()
    return int(i)


def actions(number, a = []):
    for i in range(2, number+1):
        k = 0
        for j in range(1, i+1):
            if i % j == 0:
                k += 1
        if k == 2:
            a.append(i)
    return a


def output(f1, numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    for i in range(len(numbers)):
        f1.write(f'{numbers[i]} ')


def main():
    if os.path.exists("input.txt"):
        f = open("input.txt", "r")
        number = find(f)
        numbers = actions(number)
        f1 = open("output.txt", "w")
        output(f1, numbers)
        f.close()
        f1.close()
    else:
        print('Файл с входными данными не обнаружен')


if __name__ == "__main__":
    main()
