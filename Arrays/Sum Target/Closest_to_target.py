def sum_closest(arr, target):
    n = len(arr)
    arr.sort()
    
    res = []
    diff = float('inf')
    
    left, right = 0, n - 1
    
    while left < right:
        curr = arr[left] + arr[right]
        
        if abs(target - curr) < diff:
            diff = abs(target - curr)
            res = [arr[left], arr[right]]
        
        if curr < target:
            left += 1
        elif curr > target:
            right -= 1
        else:
            return [arr[left], arr[right]]  # exact match found
        
    return res



arr = [10, 30, 20, 5]
target = 25
print(sum_closest(arr, target))  # Output: [5, 20]

# Explanation:
# The closest pair to the target sum of 25 is (5, 20), which sums to 25.
# The output is [5, 20], which is the closest pair to the target sum of 25.

arr = [5, 2, 7, 1, 4]
target = 10
print(sum_closest(arr, target))  # Output: [2, 7]

# Explanation:
#As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target. 