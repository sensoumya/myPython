'''
The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.'''
import random


def sel_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        if arr[i] != min(arr[i:]):
            j = arr.index(min(arr[i:]))
            arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = random.sample(range(1, 100), 20)
print(sel_sort(arr))
