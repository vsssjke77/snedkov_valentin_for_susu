import sorts
import time
import random


def method1(array, array_reversed, array_sorted):
    time1 = time.time()
    sorts.exchange_sorting(array)
    time1 = time.time() - time1
    time2 = time.time()
    sorts.exchange_sorting(array_sorted)
    time2 = time.time() - time2
    time3 = time.time()
    sorts.exchange_sorting(array_reversed)
    time3 = time.time() - time3
    return time1, time2, time3


def method2(array, array_reversed, array_sorted):
    time1 = time.time()
    sorts.sorting_by_choice(array)
    time1 = time.time() - time1
    time2 = time.time()
    sorts.sorting_by_choice(array_sorted)
    time2 = time.time() - time2
    time3 = time.time()
    sorts.sorting_by_choice(array_reversed)
    time3 = time.time() - time3
    return time1, time2, time3


def method3(array, array_reversed, array_sorted):
    time1 = time.time()
    sorts.fast_sort(array, 0, len(array) - 1)
    time1 = time.time() - time1
    time2 = time.time()
    sorts.fast_sort(array_sorted, 0, len(array) - 1)
    time2 = time.time() - time2
    time3 = time.time()
    sorts.fast_sort(array_reversed, 0, len(array) - 1)
    time3 = time.time() - time3
    return time1, time2, time3


def method4(array, array_reversed, array_sorted):
    time1 = time.time()
    array.sort()
    time1 = time.time() - time1
    time2 = time.time()
    array_sorted.sort()
    time2 = time.time() - time2
    time3 = time.time()
    array_reversed.sort()
    time3 = time.time() - time3
    return time1, time2, time3


def output(f, N, time1_1, time1_2, time1_3, time2_1, time2_2, time2_3, time3_1, time3_2, time3_3, time4_1, time4_2,
           time4_3, array):
    f.write(f"{'Обменная сортировка сортировка:':32} отсортированная - {time1_2:10.10f}, случайная - {time1_1:10.10f}, "
            f"отсортированная в обратном порядке - {time1_3:10.10f}\n")
    f.write(f"{'Сортировка выбором:':32} отсортированная - {time2_2:10.10f}, случайная - {time2_1:10.10f}, "
            f"отсортированная в обратном порядке - {time2_3:10.10f}\n")
    f.write(f"{'Быстрая сортировка:':32} отсортированная - {time3_2:10.10f}, случайная - {time3_1:10.10f}, "
            f"отсортированная в обратном порядке - {time3_3:10.10f}\n")
    f.write(f"{'Встроенная сортировка:':32} отсортированная - {time4_2:10.10f}, случайная - {time4_1:10.10f}, "
            f"отсортированная в обратном порядке - {time4_3:10.10f}\n")


def main():
    f = open("output.txt", 'w')
    N = int(input())
    array = [random.randint(1, N) for i in range(N)]
    f.write(f"Количество элементов: {N}\n")
    f.write(f"Cлучайная последовательность, сгенерированная программно: {array}\n")
    array_sorted = sorted(array)
    array_reversed = sorted(array, reverse=True)
    time1_1, time1_2, time1_3 = method1(array, array_reversed, array_sorted)
    time2_1, time2_2, time2_3 = method2(array, array_reversed, array_sorted)
    time3_1, time3_2, time3_3 = method3(array, array_reversed, array_sorted)
    time4_1, time4_2, time4_3 = method3(array, array_reversed, array_sorted)
    output(f, N, time1_1, time1_2, time1_3, time2_1, time2_2, time2_3, time3_1, time3_2, time3_3, time4_1, time4_2,
           time4_3, array)
    f.close()


if __name__ == "__main__":
    main()
