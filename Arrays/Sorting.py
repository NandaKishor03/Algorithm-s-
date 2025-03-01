#     # Sorting algorithms are used to arrange elements in a specific order, either ascending or descending. Here are some common sorting algorithms implemented in Python:


# ### Bubble Sort
# # Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
    

# ### Selection Sort
# # Selection sort is an in-place comparison-based sorting algorithm in which the list is divided into two parts the sorted part at the left (from index 0 to i) and the unsorted partat the right (from index i+1 to the end).In every pass, the smallest element from the unsorted part is picked and moved to the sorted part.
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
            

# ###  Insertion Sort
# # Insertion sort is a simple sorting algorithm that works much like the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j] :
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
        

# ### Quick Sort
# # Quick sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)


# ### Merge Sort
# # Merge sort is a divide-and-conquer algorithm. It works by splitting the input list into two halves, recursively sorting each half and then merging the two sorted halves into a single sorted list.
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         L = arr[:mid]
#         R = arr[mid:]
#         merge_sort(L)
#         merge_sort(R)
#         i = j = k = 0
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#     return arr    



# # arr = [64, 34, 25, 12, 22, 11, 90]
# # print("Original array:", arr)
# # print("Sorted array (Bubble Sort):", bubble_sort(arr[:]))
# # print("Sorted array (Selection Sort):", selection_sort(arr[:]))
# # print("Sorted array (Insertion Sort):", insertion_sort(arr[:]))
# # print("Sorted array (Merge Sort):", merge_sort(arr[:]))
# # print("Sorted array (Quick Sort):", quick_sort(arr[:]))


# ### Output
# # Original array: [64, 34, 25, 12, 22, 11, 90]
# # Sorted array (Bubble Sort): [11, 12, 22, 25, 34, 64, 90]
# # Sorted array (Selection Sort): [11, 12, 22, 25, 34, 64, 90]
# # Sorted array (Insertion Sort): [11, 12, 22, 25, 34, 64, 90]
# # Sorted array (Merge Sort): [11, 12, 22, 25, 34, 64, 90]
# # Sorted array (Quick Sort): [11, 12, 22, 25, 34, 64, 90]




# ### Heap sort
# #The heapq module in Python provides an implementation of the heap queue algorithm, also known as a priority queue algorithm. 
# #Heap sort is a comparison-based sorting technique based on a binary heap data structure. 
# # It is similar to the selection sort where we first find the maximum element and place the maximum element at the end. 
# # It supports min-heaps by default but can be adapted for max-heaps using negative values.

# # Heapq Methods:
# # heapify: Turns a list into a heap in-place.
# # heappush: Adds an item to the heap.
# # heappop: Removes and returns the smallest item from the heap.
# # heappushpop: Adds an item and then removes the smallest item.
# # heapreplace: Removes the smallest item and then adds a new item.
# # nlargest: Retrieves the n largest elements from an iterable.
# # nsmallest: Retrieves the n smallest elements from an iterable.

# # MIN-HEAPQ
# import heapq
# def main():
#     arr = [4, 3, 2, 5, 1, 9, 8, 0]

#     # Convert the array into a min-heap
#     heapq.heapify(arr)
#     print("Min-Heap:", arr)

#     # Push a new item onto the heap
#     new_item = -1
#     heapq.heappush(arr, new_item)
#     print(f"Min-Heap after adding {new_item}:", arr)

#     # Pop the smallest item from the heap
#     smallest = heapq.heappop(arr)
#     print(f"Smallest item popped: {smallest}")
#     print("Min-Heap after popping the smallest item:", arr)

#     # Example of heapreplace (pop and push in one operation)
#     heapq.heapreplace(arr, 10)
#     print("Min-Heap after heapreplace with 10:", arr)

#     # Example of heappushpop (push and pop in one operation)
#     pushed_and_popped = heapq.heappushpop(arr, 7)
#     print(f"Pushed 7 and popped {pushed_and_popped}")
#     print("Min-Heap after heappushpop:", arr)

#     # Finding n smallest elements
#     smallest_elements = heapq.nsmallest(3, arr)
#     print("Three smallest elements:", smallest_elements)

#     # Finding n largest elements
#     largest_elements = heapq.nlargest(3, arr)
#     print("Three largest elements:", largest_elements)

# # if __name__ == "__main__":
#     # main()



# #MAX HEAPQ
# import heapq
# def pop_max_elements(neg_arr):
#     max_elements = []
#     while neg_arr:
#         max_elements.append(-heapq.heappop(neg_arr))
#     print(max_elements)

# arr = [4,3,2,5,1,9,8,0]
# neg_arr = [-x for x in arr]
# heapq.heapify(neg_arr)
# pop_max_elements(neg_arr)


# ### If you want to sort the array for every iteration of the loop then use "HEAPQ"
# # import heapq
# # # arr = [4,3,2,5]
# # arr = [4,3,2,5,1,9,8,0]
# # heapq.heapify(arr)
# # while len(arr) > 0:
# #     print(heapq.heappop(arr))   OUTPUT print the elements samllest to largest


# # Example for heapq  -----  Minimum cost of the ropes
# def minCost(arr):
#     heapq.heapify(arr)
#     count = 0
#     while (len(arr) > 1):
#         first = heapq.heappop(arr)
#         second = heapq.heappop(arr)    
#         res = first + second        
#         count += res
#         heapq.heappush(arr,res)            
#     return count 
# arr = [4,3,2,5]
# # print(minCost(arr))


# 

x = [i for i in range(10) if i%2 == 1]
print(x)