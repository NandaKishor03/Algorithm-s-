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


### Prime number or not
# import math
# def Prime(n):
#   flag = True
#   for i in range(2,math.ceil(n**0.5)):
#       if n % i == 0:
#           flag = False
#           break
#   if flag == True: 
#       print("Prime")
#   else:
#       print("Not a Prime")
#Prime(9)
#Prime(11)


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

### Reverse a Array
# arr = [2,3,4,5,3,5,6,7,0]
# n = len(arr)
# i = 0
# while i < n//2 :
#     arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]
#     i += 1
# print(arr) 


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
import heapq
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
# # a = [1,2,3,4]    -----   [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
# a = [12,28,83,4,25,26,25,2,25,25,25,12]
# a = [2,3,4,5,6]
# a.sort()
# n = len(a)
# subset = []
# for i in range(0,(1<<n)):
#     b = []
#     for bit in range(0,n):
#         if (i & (1<< bit)):
#             b.append(a[bit])
#     subset.append(b)
# print(subset)
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



### Valid Parentheses
# def is_valid(s: str) -> bool:
#     stack = []
#     check = True
#     for char in s:
#         if char in '({[':
#             stack.append(char)
#         else:
#             if stack:
#                 t = stack.pop()
#                 if (char == ')' and t != '(') or (char == '}' and t != '{') or (char == ']' and t != '['):
#                     check = False
#                     break
#             else:
#                 check = False
#                 break
#     return (len(stack) == 0 and check)
# print( is_valid("(({}]))"))



# Number steps to Convert the number to 1 using:
# -> Divide the number by the factors (apart from 1 and n)
# ->Substract 1 from the number
# n = 90    # 2
# n = 91    # 3
# n = 50    # 2
# if n>=4:
#     if n%2 == 0:
#         print(2)
#     else:
#         print(3)
# else:
#     print(n-1)


### Best Grade
# find the Maximized garde with lexographically smallest character grade to the Pth Index in atmost k Swaps
def best(arr,p,k):
# Method - 1
    # p -= 1
    # best_grade = arr[p-k:p+k]
    # print(min(best_grade))
# Method - 2
    char = arr[p-1]
    for i in range(p,min(len(arr),p+k)):
        if char > arr[i]:
            char = arr[i]
    for i in range(max(0,p-k-1),p-1):
        if char > arr[i]:
            char = arr[i]
    print(char)
# arr = "abffbcdehjfg"
# p=3
# k=4
# best(arr,p,k)


### Minimum no of key presses to get number
# initail value 0
# you can press [0,1,2,3,4,5,6,7,8,9,00]
# if we press 00 the number will become
def min_press(n):
    i , keys = 0 , 0
    while i < len(n):
        if i < len(n) -1 and n[i] == '0' and n[i+1] =='0':
            i += 2
            keys += 1
        else:
             i += 1
             keys += 1
    print(keys)
# min_press('100')
# min_press('12300')
# min_press('1020')
# min_press('1001')


### Longest Substring with Even Length
# String contains numbers from 0 to 9
# sum of the left k digits is equal to sum of the right k digits
# else, print 0
# def sum(s):
#     res = 0
#     for x in s:
#         res += int(x)
#     return res

# def Even_length(arr):
#     n = len(arr)
#     maxlen = 0
#     for i in range(n):
#         for j in range(i+2,n+1,2):
#             sub_string = arr[i:j]
#             t = len(sub_string)
#             left , right = sub_string[:t//2] , sub_string[t//2:]
#             if t%2 == 0 and sum(left) == sum(right):
#                 maxlen = max(maxlen,t)
#     print(maxlen)
# arr = '123123'
# arr = '1234'
# Even_length(arr)


### Longest Common Perfix
def longestCommonPrefix(strs):
    if not strs:
        return None
    perfix = strs[0]
    for s in strs[1:]:
        while not s.startswith(perfix):
            perfix = perfix[:-1]
            if not perfix:
                return None
    return perfix

strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]
# print(longestCommonPrefix(strs))


### Find K Pairs with Smallest Sums
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
# Return the Smallest sum
import heapq
def kSmallestPairs(nums1, nums2):
    if not nums1 and not nums2:
        return []
    heap = []
    for i in range(min(k,len(nums1))):
        heapq.heappush(heap,(nums1[i] + nums2[0] , i , 0))
    result = []
    while heap and len(result) < k:
        curr_sum , i , j = heapq.heappop(heap)
        result.append([nums1[i],nums2[j]])
        if j+1 < len(nums2):
            heapq.heappush(heap,(nums1[i] + nums2[j+1] , i , j+1))
    return result

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
# nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# print(kSmallestPairs(nums1,nums2))          #output : [[1, 2], [1, 4], [1, 6]]


### Continuous Subarray Sum of the Number
# Number = 91
#  -> 45 46 
#  -> 10 11 12 13 14 15 16 
#  -> 1 2 3 4 5 6 7 8 9 10 11 12 13 
def sum_numder(target):
    k = 2
    while True:
        n = (target - (k-1)*k/2)/k
        if n <= 0:
            break
        if n - int(n) == 0:
            n = int(n)
            for i in range(n,n+k):
                print(i,end=" ")
            print()
        k += 1

sum_numder(91)




### Find the Smallest Number
# Find the smallest number that can be formed by removing k digits from the number
# def removeKdigits(num, k):
#     stack = []
#     for digit in num:
#         while k and stack and stack[-1] > digit:
#             stack.pop()
#             k -= 1
#         stack.append(digit)
#     stack = stack[:-k] if k else stack
#     return "".join(stack).lstrip('0') or "0"
# num = "1432219"
# k = 3
# print(removeKdigits(num,k))

