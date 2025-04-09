def subarray_sum_k_positive(arr, k):
    left = 0
    curr_sum = 0

    for right in range(len(arr)):
        curr_sum += arr[right]
        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1
        if curr_sum == k:
            return (left, right)
    return None



def subarrayXor(self, arr, k):
    # code here
    count = 0        
    seen = {}
    perfix_xor = 0
    
    for num in arr:
        perfix_xor ^= num
        
        if perfix_xor ^ k in seen:
            count += seen.get(perfix_xor^k)
            
        if perfix_xor == k:
            count += 1
            
        seen[perfix_xor] = seen.get(perfix_xor,0)+1
        
    return count