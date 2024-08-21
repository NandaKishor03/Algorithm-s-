                            #  GEEKS FOR GEEKS and LEETCODE PROBLEM OF THE DAY  #

### check if a2 is subset of a1 or not   ---- GFG
# a1 = [11, 7, 1, 13, 21, 3, 7, 3]
# a2 = [11, 3, 7, 1, 7]

# for x in a2:
#     if x not in a1:
#         print("No")
#     else:
#         a1.remove(x)
# print("Yes")



### Sum equal to 0    ---- GFG
# lst = [-1,1,-1,1]
# res = []
# k = 1 
# while k <= len(lst):
#     for i in range(len(lst)-k+1):
#         arr1 = lst[i:i+k]
#         if sum(arr1) == 0:
#             res.append(arr1)
#     k += 1
# print(res)
# print(len(res))



###  first Element KTime  ---- GFG
# def firstElementKTime(n, k, arr):
#     dct = {}
#     for i in range(n):
#         dct[arr[i]] = i  
#     k = []
#     c = []
#     for key,count in dct.items():
#         if count >= k:
#             k.append(key)
#             c.append(count)
#     if len(res) > 1:
#         ind = c.index(min(c))
#         return k[ind]
#     else:
#         return k[-1]
# print(firstElementKTime(7 , 2, [1 ,7 ,4 ,3 ,4 ,8 ,7]))



### Validate an IP Address  ---- GFG
# def isValid(str):
#     lst = str.split(".")
#     if  len(lst) != 4:
#         return False
#     for x in lst:
#         if x[0] == '0':
#             return False
#         if int(x) < 0 or int(x) >= 255:
#             return False
#     return True
# print(isValid("01.01.01.01"))



###  Number of Senior Citizens  ----  LEETCODE 2678
# def countSeniors(details):
#     count = 0
#     for x in details:
#         if (int(x[11:13]) > 60):
#             count += 1
#         # y1 = x[11]
#         # y2 = x[12]
#         # y1 , y2 = int(y1) , int(y2)
#         # z = y1*10 + y2
#         # if z > 60:
#         #     count += 1
#     return count
# details = ["1313579440F0236","2921522980M5644"]
# print(countSeniors(details))
        


### Range Sum of Sorted Subarray Sums  ----   LEETCODE 1508
# nums = [1,2,3,4]
# n = 4
# left = 1
# right = 5
# mod = (10**9) + 7
# lst = []
# for i in range(n):
#     current_sum = 0
#     for j in range(i, n):
#         current_sum += nums[j]
#         lst.append(current_sum)
# lst.sort()
# res = 0 
# for i in range(right):
#     res +=  lst[i]
# print(res%mod)



### Domiant Cells  ---- HackerRank certify
# def numCells(grid):
#     n = len(grid)
#     m = len(grid[0])
#     def get_neighbours(i,j):
#         neighbors = []
#         directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
#         for d in directions:
#             ni , nj = i + d[0] , j +d[1]
#             if 0 <= ni < n and 0 <= nj < m:
#                 neighbors.append(grid[ni][nj])
#         return neighbors
#     count = 0
#     for i in range(n):
#         for j in range(m):
#             neighbors = get_neighbours(i,j)
#             if all(grid[i][j] > neighbor for neighbor in neighbors):
#                 count += 1
#     return count