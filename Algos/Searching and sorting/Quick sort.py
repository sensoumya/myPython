import random


def quick_sort(arr):
    quick_helper(arr, 0, len(arr) - 1)
    return arr


def quick_helper(arr, first, last):
    if first < last:
        split = partition(arr, first, last)
        quick_helper(arr, first, split - 1)
        quick_helper(arr, split + 1, last)


def partition(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last
    done = False
    while not done:
        print(arr)
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left > right:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    print(arr)
    arr[first], arr[right] = arr[right], arr[first]
    print(arr)
    return right


# arr = random.sample(range(1, 100), 20)
# print(arr)
print(quick_sort([42, 4, 6, 97, 29]))
