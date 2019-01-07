'''
The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.'''
import random


def bubb_sort(arr):
    length = len(arr)
    done = False
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                done = True
        if done == False:
            break
    return arr


arr = random.sample(range(1, 100), 20)
print(bubb_sort(arr))
