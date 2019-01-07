import random


def ins_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[:j][-1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


arr = random.sample(range(1, 100), 20)
print(arr)
print(ins_sort(arr))
