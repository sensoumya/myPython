'''
The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. This process continues and requires n−1 passes to sort n items, since the final item must be in place after the (n−1) st pass.
'''
import random


def sel_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        if arr[i] != min(arr[i:]):
            j = arr.index(min(arr[i:]))
            arr[i], arr[j] = arr[j], arr[i]
    return arr


def sel_sort(arr):
    length = len(arr)
    for i in range(length):
        min_ind = i
        for j in range(i + 1, length):
            if arr[min_ind] > arr[j]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr


arr = random.sample(range(1, 100), 20)
print(sel_sort(arr))
