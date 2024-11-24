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


### Mirror Tree Logic   ----  GFG
# def Mirror(self,root):
#         if root is None:
#             return None
#         root.left, root.right = root.right, root.left
#         self.mirror(root.left)
#         self.mirror(root.right)
#         return root



### XOR Queries of a Subarray  ----- Leetcode 1310
#  Brute-force
# arr = [1,3,4,8]
# queries = [[0,1],[1,2],[0,3],[3,3]]
# lst = []
# for x in queries:
#     c = 0
#     for i  in range(x[0],x[1]+1):
#         c ^= arr[i]
#     lst.append(c)
# return lst

#  Optimized 
# prefix_xor = [0] * (len(arr) + 1)
# for i in range(len(arr)):
#         prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
# result = [prefix_xor[r + 1] ^ prefix_xor[l] for l, r in queries]
#         print(result)



### Alernative positive and negative Number  ----- GFG
# arr = [9, 4, -2, -1, 5, 0, -5, -3, 2
# arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# pos = [num for num in arr if num >= 0]
# neg = [num for num in arr if num < 0]
# result = []
# pos_index, neg_index = 0, 0
# while pos_index < len(pos) and neg_index < len(neg):
#     result.append(pos[pos_index])
#     pos_index += 1
#     result.append(neg[neg_index])
#     neg_index += 1
# result.extend(pos[pos_index:])
# result.extend(neg[neg_index:])
# print(result)



### In-Place Binary Tree to Double Linked List Convertion  -----  GFG
# def bToDLL(self, root):
#     prev = None
#     head = None
#     def inorder(node):
#         nonlocal prev, head
#         if node:
#             inorder(node.left)
#             if prev is None:
#                 head = node
#             else:
#                 node.left = prev
#                 prev.right = node
#             prev = node
#             inorder(node.right)
#     inorder(root)
#     return head


###  Rotate and delete ----- GFG
# arr = [1, 2, 3, 4, 5, 6]
# a = len(arr)
# i = 1
# while a > 1:
#     num = arr.pop()
#     arr.insert(0,num)
#     if len(arr) > i:
#         arr.pop(-i)
#     else:
#         arr.pop(0)
#     i += 1
#     a = len(arr)
# print(arr[0])



### Next Permutation of the Number
def next_permutation(arr):
    n = len(arr)
    # Find the pivot index
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    # If pivot point does not exist, 
    # reverse the whole array
    if pivot == -1:
        arr.reverse()
        return
    # Find the element from the right 
    # that is greater than pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break
    # Reverse the elements from pivot + 1 to the end in place
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
# arr = [ 2, 4, 1, 7, 5, 0 ]      ### 2 4 5 0 1 7
# arr = [ 2, 7, 1, 4, 5, 0 ]      ### 2 7 1 5 0 4
# arr = [ 1, 7, 5, 4, 2, 0 ]      ### 2 0 1 4 5 7
# next_permutation(arr)
# print(" ".join(map(str, arr)))


### Level Order Traversal of the Binary Tree

# def level_order(root):
#     q = []
#     q.append(root)
#     while root:
#         if 