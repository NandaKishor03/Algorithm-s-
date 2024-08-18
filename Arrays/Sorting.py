    # Sorting algorithms are used to arrange elements in a specific order, either ascending or descending. Here are some common sorting algorithms implemented in Python:


### Bubble Sort
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    

### Selection Sort
# Selection sort is an in-place comparison-based sorting algorithm in which the list is divided into two parts the sorted part at the left (from index 0 to i) and the unsorted partat the right (from index i+1 to the end).In every pass, the smallest element from the unsorted part is picked and moved to the sorted part.
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
            

###  Insertion Sort
# Insertion sort is a simple sorting algorithm that works much like the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
        

### Quick Sort
# Quick sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


### Merge Sort
# Merge sort is a divide-and-conquer algorithm that was invented by John von Neumann in
# 1945. It works by splitting the input list into two halves, recursively sorting each half
# and then merging the two sorted halves into a single sorted list.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
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
            k += 1
    return arr    



arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Sorted array (Bubble Sort):", bubble_sort(arr[:]))
print("Sorted array (Selection Sort):", selection_sort(arr[:]))
print("Sorted array (Insertion Sort):", insertion_sort(arr[:]))
print("Sorted array (Merge Sort):", merge_sort(arr[:]))
print("Sorted array (Quick Sort):", quick_sort(arr[:]))


### Output
# Original array: [64, 34, 25, 12, 22, 11, 90]
# Sorted array (Bubble Sort): [11, 12, 22, 25, 34, 64, 90]
# Sorted array (Selection Sort): [11, 12, 22, 25, 34, 64, 90]
# Sorted array (Insertion Sort): [11, 12, 22, 25, 34, 64, 90]
# Sorted array (Merge Sort): [11, 12, 22, 25, 34, 64, 90]
# Sorted array (Quick Sort): [11, 12, 22, 25, 34, 64, 90]