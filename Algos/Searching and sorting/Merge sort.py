import random


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l_arr = arr[:mid]
        r_arr = arr[mid:]

        merge_sort(l_arr)
        merge_sort(r_arr)

        i, j, k = 0, 0, 0

        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = r_arr[j]
                j += 1
                k += 1

        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1
    return arr


# arr = random.sample(range(1, 100), 20)
# print(arr)
print(merge_sort([42, 4, 6, 97, 29]))
