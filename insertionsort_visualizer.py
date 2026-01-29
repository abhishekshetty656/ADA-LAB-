import matplotlib.pyplot as plt
import random
import time

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
print("Sorted list:", insertion_sort(l.copy()))



n_list = [5000, 6000, 7000, 8000, 9000, 10000]
sort_time = []

for n in n_list:
    arr = [random.randint(1, 10000) for _ in range(n)]

    start = time.perf_counter()
    insertion_sort(arr)
    end = time.perf_counter()

    sort_time.append(end - start)



plt.plot(n_list, sort_time, marker='o')
plt.xlabel('n (input size)')
plt.ylabel('Time (seconds)')
plt.title('Insertion Sort Time Complexity')
plt.grid(True)
plt.show()
