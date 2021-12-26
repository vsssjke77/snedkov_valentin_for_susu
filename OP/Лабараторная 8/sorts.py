def exchange_sorting(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    return


def sorting_by_choice(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
    return


def fast_sort(nums, x, y):
    if x >= y:
        return
    i = x
    j = y
    bar = nums[i + (j - i) // 2]
    while i <= j:
        while nums[i] < bar:
            i += 1
        while nums[j] > bar:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    fast_sort(nums, x, j)
    fast_sort(nums, i, y)
