import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


l = [random.randint(1, 100) for _ in range(10)]
print("Original list:", l)
print("Sorted list:", insertion_sort(l))