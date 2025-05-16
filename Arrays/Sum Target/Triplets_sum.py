def count_triplets(arr, target):
    arr.sort()  
    n = len(arr)
    pairs = 0

    for i in range(n - 2):
        j = i + 1
        k = n - 1

        while j < k:
            total = arr[i] + arr[j] + arr[k]

            if total < target:
                j += 1
            elif total > target:
                k -= 1
            else:
                ele1 = arr[j]
                ele2 = arr[k]
                count1 = 0
                count2 = 0

                if ele1 == ele2:
                    count = k - j + 1
                    pairs += (count * (count - 1)) // 2
                    break

                while j <= k and arr[j] == ele1:
                    count1 += 1
                    j += 1

                while j <= k and arr[k] == ele2:
                    count2 += 1
                    k -= 1

                pairs += count1 * count2

    return pairs

arr = [-3, -1, -1, 0, 1, 2]
target = -2
print(count_triplets(arr, target))  # Output: 4


# Explanation:
# The triplets whose sum is equal to -2 are:
# 1. (-3, -1, 2)
# 2. (-3, 0, 1)
# 3. (-1, -1, 0)
# 4. (-1, 0, -1)

# The output is 4, which is the count of triplets whose sum is equal to -2.