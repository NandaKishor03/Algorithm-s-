def sum_less_than_target(arr,target):
    arr.sort()

    count = 0
    left , right = 0 , len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum < target:
            count += right - left
            left += 1
        else:
            right -= 1

    return count

arr = [7, 2, 5, 3]
target = 8
print(sum_less_than_target(arr, target))  # Output: 4

# Explanation:
# The pairs whose sum is less than 8 are:
