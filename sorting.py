import numpy as np
# selection sorting

def select_sort(arr):
    for i in range(len(arr)):
        MinIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[MinIndex]:
                MinIndex = j
        arr[i], arr[MinIndex] = arr[MinIndex], arr[i]
    return arr


arr = np.random.randint(10, 100, 10)
print(arr)



# insertion sorting

def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


def bubble_sort(arr):

    Already_sorted = True
    while Already_sorted:
        Already_sorted =
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


print(select_sort(arr))
print(insert_sort(arr))