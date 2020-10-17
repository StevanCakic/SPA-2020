def merge_sort(arr):
    if len(arr) > 1:
        # Trazenje srednjeg elementa niza, tj. indeksa
        mid = len(arr) // 2

        # Split
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        # Merge
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k +=1
 
def partion(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1 

def quick_sort(arr, low, high):
    if low < high:
        p = partion(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p+1, high)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(arr)
# quick_sort(arr, 0, len(arr) - 1)
heap_sort(arr)
print(arr)
