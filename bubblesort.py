def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input("Enter the value of n: "))
lst = []

for i in range(n):
    lst.append(int(input(f"Enter element [{i + 1}]: ")))

bubble_sort(lst)
print("Sorted list:", lst)
