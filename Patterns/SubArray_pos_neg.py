def count_subarrays_with_sum_k(arr, k):
    prefix_sum = 0
    count = 0
    seen = {0: 1}
    
    for num in arr:
        prefix_sum += num
        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count

# Test it
arr = [10, 2, -2, -20, 10]
k = -10
print(count_subarrays_with_sum_k(arr, k))  # Output: 3





# Step-by-Step for Each Index:      

# Step 0:
# num = 10
# prefix_sum += 10 → 10
# Check: prefix_sum - k = 10 - (-10) = 20
# 20 not in seen, so no subarray ends here with sum = -10
# Update seen: {0: 1, 10: 1}
# count = 0


# Step 1:
# num = 2
# prefix_sum += 2 → 12
# Check: prefix_sum - k = 12 - (-10) = 22
# 22 not in seen, no subarray
# Update seen: {0: 1, 10: 1, 12: 1}
# count = 0


# Step 2:
# num = -2
# prefix_sum += -2 → 10
# Check: prefix_sum - k = 10 - (-10) = 20
# 20 not in seen
# Update seen: {0: 1, 10: 2, 12: 1}
# count = 0


# Step 3:
# num = -20
# prefix_sum += -20 → -10
# Check: prefix_sum - k = -10 - (-10) = 0
# 0 is in seen → seen[0] = 1
# This means there’s 1 subarray ending at index 3 with sum = -10
# So: count += 1 → count = 1
# Update seen: {0: 1, 10: 2, 12: 1, -10: 1}
# Subarray found: [10, 2, -2, -20] → sum = -10


# Step 4:
# num = 10
# prefix_sum += 10 → 0
# Check: prefix_sum - k = 0 - (-10) = 10
# 10 is in seen → seen[10] = 2
# So, 2 subarrays end here with sum = -10
# count += 2 → count = 3
# Update seen: {0: 2, 10: 2, 12: 1, -10: 1}


# Subarrays found:
# [2, -2, -20, 10] (index 1 to 4)
# [-20, 10] (index 3 to 4)
# Final Output: count = 3


# So there are 3 subarrays with sum = -10

# [10, 2, -2, -20] → sum = -10 (indices 0 to 3)

# [2, -2, -20, 10] → sum = -10 (indices 1 to 4)

# [-20, 10] → sum = -10 (indices 3 to 4)