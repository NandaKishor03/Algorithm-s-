### Binary to Integer
# a1 = 100000100000
# count = 0
# while  a1 > 0:
#     count = (count * 2) + a1 % 10
#     a1 //= 10
# print("Binary ",a1 ," to Integer ",count)


### Integer to Binary
# a2 = 2080
# a2 = 2
# a2 = 29
# b2 = bin(a2)[2:]
# print("Integer ",a2, " to Binary ",b2)


### Roman to Integer
arr = "MCMXVII"
def RomanToInteger(s):
    dct = {"I":1 , "V":5 , "X":10 , "L":50 , "C":100 , "D":500 , "M":1000 , "IV":4 , 
    "IX":9 , "XL":40 , "XC":90 , "CD":400 , "CM":900}
    lst = []
    i = 0
    j = len(s)
    new = ""
    while i < j:
        if s[i:i+2] in dct:
            new = s[i:i+2]
            lst.append(dct[new])
            i += 2
        elif s[i] in dct:
            lst.append(dct[s[i]])
            i += 1
    return sum(lst)


### Mirror Tree Logic
def mirror(root):
    if root is None:
        return None
    root.left , root.right = root.right , root.left
    mirror(root.left)
    mirror(root.right)
    return root


# ### Methods to Remove leading Zeros for String or Number.
# # Using str.lstrip('0')
# s = "00012345"
# s = s.lstrip('0')
# print(s)  # Output: "12345"

# # Using int()
# s = "00012345"
# s = str(int(s))
# print(s)  # Output: "12345"

# # Handling all zeros case with int()
# s = "0000"
# s = str(int(s))
# print(s)  # Output: "0"


### If you want to sort the array for every iteration of the loop then use "HEAPQ"
# Example - Minimum cost of ropes
def minCost(arr):
    heapq.heapify(arr)
    count = 0
    while (len(arr) > 1):
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)    
        res = first + second        
        count += res
        heapq.heappush(arr,res)            
    return count 


# import math
### Subsets of the Array   
# a = [1,3,2]     -----   [[], [1], [3], [1, 3], [2], [1, 2], [3, 2], [1, 3, 2]]
# a = [1,2,3,4]    -----   [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
# a = [12,28,83,4,25,26,25,2,25,25,25,12]
# a.sort()
# n = len(a)
# subset = []
# for i in range(0,(1<<n)):
#     b = []
#     for bit in range(0,n):
#         if (i & (1<< bit)):
#             b.append(a[bit])
#     subset.append(b)
# lst = []
# for x in subset:
#     if sum(x) == 213:
#         lst.append(len(x))
# print(lst)





### Perfix_sum of the Array with queres "Sum of Query II"
def querySum( n, arr, q, queries):
    prefix_sum = [0] * (n + 1)    
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    result = []      
    for i in range(q):
        l = queries[2 * i]
        r = queries[2 * i + 1]
        sum_lr = prefix_sum[r] - prefix_sum[l - 1]
        result.append(sum_lr)
    print(result)
n = 4
arr = [1, 2, 3, 4]
q = 2
queries = [1, 4, 2, 3]
# querySum(n, arr, q, queries)  -----   [10, 5]



### Prime Factors of the given number
def PrimeFactors(num):
    lst  = []
    factor = 2
    while (num >= 2):
        if (num % factor == 0):
            lst.append(factor)
            num = num / factor
        else:
            factor += 1
    lst.sort()
    return lst
# print(PrimeFactors(125))  ###[5,5,5]
# print(PrimeFactors(136))  ###[2,2,2,17]



### Factors of the Number 
def kThSmallestFactor(num):
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)
        print(factors)                        ### [1, 120, 2, 60, 3, 40, 4, 30, 5, 24, 6, 20, 8, 15, 10, 12]
    
    factors.sort()
    print(factors)              ###  [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]
# kThSmallestFactor(120)



### Move all Zeos's to the end of the array
def Move_Zero(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow] , arr[fast] = arr[fast] , arr[slow]
            slow += 1
    return arr
# arr = [1, 2, 0, 4, 3, 0, 5, 0]
# print(Move_Zero(arr))           ----   [1, 2, 4, 3, 5, 0, 0, 0]
# arr = [3,3,0,0,4]
# print(Move_Zero(arr))       ----    [3, 3, 4, 0, 0]



### Maximum Subarray Sum using Kadane's Algorithm
arr = [2, 3, -8, 7, -1, 2, 3]
res = arr[0]
end = arr[0]
for i in range(1,len(arr)):
    end = max(arr[i] , end+arr[i])      ###  5 -3 7 6 8 11 
    res = max(res , end)                ###  5 5 7 7 8 11 

print(max(res,end))    ###  11



### Find the Single Digit Sum of a Number.
def findSingle(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9
# n = 5674                    # 4
n = 1234                    # 1
# print(findSingle(n))