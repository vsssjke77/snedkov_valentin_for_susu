# 1 задание
razmer_file = int(input("Введите размер файла в байтах"))
razmer_k_file  = razmer_file//1024
print("Размер фалйла в килобайтах составляет", razmer_k_file)


#2 задание
first = ''
second = ''
third = ''
m = str(input())
if m[0] == '1':
    first = 'Сто'
    if m[1] == '0':
        if m[2] == '0':
            print(first,second,third)
        if m[2] == '1':
            third = 'один'
            print(first, second, third)
        if m[2] == '2':
            third = 'два'
            print(first, second, third)
        if m[2] == '3':
            third = 'три'
            print(first, second, third)
        if m[2] == '4':
            third = 'четыре'
            print(first, second, third)
        if m[2] == '5':
            third = 'пять'
            print(first, second, third)
        if m[2] == '6':
            third = 'шесть'
            print(first, second, third)
        if m[2] == '7':
            third = 'семь'
            print(first, second, third)
        if m[2] == '8':
            third = 'восемь'
            print(first, second, third)
        if m[2] == '9':
            third = 'девять'
            print(first, second, third)
    if m[1] == '1':
        if m[2] == '1':
            second = 'одиннацать'

#3
p=1
A = int(input())
B = int(input())
if A < B:
    for i in range(A,B+1):
        p*=i
print(p)