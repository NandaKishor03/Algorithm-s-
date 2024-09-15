#   Searching Algorithms are used to locate a specific element in an array.

### Linear Search
# Time Complexity: O(n)
# Description: The simplest search algorithm that checks every element in the array until the desired element is found or the end of the array is reached.
# Use Case: Works well for unsorted or small arrays.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element
    return -1  # Return -1 if the target element is not found



### Binary Search
# Time Complexity: O(log n)
# Description: A fast search algorithm that works on sorted arrays by repeatedly dividing the search interval in half until the desired element is found.
# Use Case: Works well for large sorted arrays.
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target element
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if the target element is not found


arr = [25,20,8,99,56,66,6]
target = 6
print("Liner Search : ",liner_search(arr,target))
print("Binary Search : ",binary_search(arr,target))


### Output
# Liner Search : 7
# Binary Search : 7

        
    

#   Searching Algorithms are used to locate a specific element in an array.

### Linear Search
# Time Complexity: O(n)
# Description: The simplest search algorithm that checks every element in the array until the desired element is found or the end of the array is reached.
# Use Case: Works well for unsorted or small arrays.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element
    return -1  # Return -1 if the target element is not found



### Binary Search
# Time Complexity: O(log n)
# Description: A fast search algorithm that works on sorted arrays by repeatedly dividing the search interval in half until the desired element is found.
# Use Case: Works well for large sorted arrays.
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target element
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if the target element is not found



### Modified Binary Search
