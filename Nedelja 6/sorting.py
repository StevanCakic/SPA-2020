
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                '''tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp'''
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(selection_sort([4, 2, 3, 1]))
print(bubble_sort([4, 3, 1, 2]))
