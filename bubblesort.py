import random
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
arr = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]

print(arr)
print(bubbleSort(arr))
