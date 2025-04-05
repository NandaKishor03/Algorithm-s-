# Sliding Window Technique is a method used to efficiently solve problems that involve defining a window or range in the input data (arrays or strings) and then moving that window across the data to perform some operation within the window. This technique is commonly used in algorithms like finding subarrays with a specific sum, finding the longest substring with unique characters, or solving problems that require a fixed-size window to process elements efficiently.

# There are basically two types of sliding window:

# 1. Fixed Size Sliding Window:
# The general steps to solve these questions by following below steps:

# Find the size of the window required, say K.
# Compute the result for 1st window, i.e. include the first K elements of the data structure.
# Then use a loop to slide the window by 1 and keep computing the result window by window.
# 2. Variable Size Sliding Window:
# The general steps to solve these questions by following below steps:

# In this type of sliding window problem, we increase our right pointer one by one till our condition is true.
# At any step if our condition does not match, we shrink the size of our window by increasing left pointer.
# Again, when our condition satisfies, we start increasing the right pointer and follow step 1.
# We follow these steps until we reach to the end of the array.


def fixed_size_sliding_window(arr, k):
  n = len(arr)
  if n < k:
    return []

  window_sum = sum(arr[:k])
  max_sum = window_sum

  for i in range(n - k):
    print(i)
    window_sum = window_sum - arr[i] + arr[i + k]
    max_sum = max(max_sum, window_sum)

  return max_sum

arr = [1, 3, 2, 5, 1, 1, 2, 3]
k = 3
# print(fixed_size_sliding_window(arr, k))  # Output: 10




def variable_size_sliding_window(arr, target):
  n = len(arr)
  left = 0
  current_sum = 0
  min_length = float('inf')

  for right in range(n):
    current_sum += arr[right]

    while current_sum >= target:
      min_length = min(min_length, right - left + 1)
      current_sum -= arr[left]
      left += 1

  return min_length if min_length != float('inf') else 0

arr = [2, 3, 1, 2, 4, 3]
target = 7
print(variable_size_sliding_window(arr, target))  # Output: 2