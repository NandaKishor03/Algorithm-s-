### Longest Palindrome SubArray Length
# def LongestPalindrome(s):
#     res=""
#     s2=0
#     if(S==S[::-1]):
#         return (S)
#     for i in range(len(S)):
#         st=''
#         s1=0
#         for j in range(i,len(S)):
#             st+=S[j]
#             s1+=1
#             if(st==st[::-1]):
#                 if(s1>s2):
#                     res=st
#                     s2=s1
#     return res



# def LongestPalindrome(s):
#     lp = ""
    # dp = [[False]*len(s) for _ in range(len(s))]
#     for i in range(len(s)):
#         dp[i][i] = True
#         lp = s[i]
#     for i in range(len(s)-1 , -1 , -1):
#         for j in range(i+1 , len(s)):
#             if s[i] == s[j]:
#                 if j - i == 1 or dp[i+1][j-1] is True:
#                     dp[i][j] = True
#                     if len(lp) < len(s[i:j+1]):
#                         lp = s[i:j+1]
#     return lp



### In-Place Binary Tree to Double Linked List Convertion 
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



### Robot Movements for the position in the grid based on Right and Left moves with the Directions(N,E,S,W)
grid_x , grid_y = 3 , 3
ins = ['R','M','L','M','L','M']
# grid_x , grid_y = 3 , 4
# ins = ['R','M','L','M','L','M','R','M']
x , y , facing = 2 , 2 , 'E'
output_string = ""
def next_facing(curr_facing , move):
    directions = {'N':['W','E'] , 'S' :['E' , 'W'] , 'W' : ['S', 'N'] , 'E' : ['N' , 'S']}
    if move == 'R':
        return directions.get(curr_face)[1]
    else:
        return directions.get(curr_face)[0]
curr_x , curr_y , curr_face = x , y , facing
for x in ins:
    if x == 'R' or x == 'L':
        curr_face = next_facing(curr_face , x)
        continue
    elif x == 'M':
        if curr_face == 'N':
            i , j = 0 , 1
        elif curr_face == 'E':
            i , j = 1, 0
        elif curr_face == 'S':
            i , j = 0, -1
        elif curr_face == 'W':
            i , j = -1 , 0
        if (curr_x + i) > grid_x or (curr_y + j ) > grid_y or (curr_x + i ) <= 0 or (curr_y + j) <= 0 :
            # print(str(curr_x)+'-'+str(curr_y)+'-'+str(curr_face)+'-ER')
            output_string += "-ER"
            break
        curr_x = curr_x + i
        curr_y = curr_y + j
print(str(curr_x)+'-'+str(curr_y)+'-'+str(curr_face) + output_string)



### Remove one character and check if the string is palindrome or not palindrome
# arr = 'nandganan'
# flag = True
# i , j = 0 , len(arr) -1
# while i < j:
#     if arr[i] == arr[j]:
#         i += 1
#         j -= 1
#     else:
#         new_arr = arr[:i] + arr[j:]
#         if new_arr != new_arr[::-1]:
#             print("Not Palindrome")
#         else:
#             new_arr = arr[:j] + arr[j+1:]
#             if new_arr != new_arr[::-1]:
#                 print("Not Palindrome")
#         break
# print("palindrome")



###  Minimize the maximum difference between the heights
# def getMinDiff(arr, k):
#     n = len(arr)
#     arr.sort()                      ###  [4, 6, 10, 12, 15, 17] 
#     res = arr[n - 1] - arr[0]       ### res = 13
#     for i in range(1, len(arr)):
#         if arr[i] - k < 0:
#             continue
#         minH = min(arr[0] + k, arr[i] - k)             ###  0 4 6 9 10 
#         maxH = max(arr[i - 1] + k, arr[n - 1] - k)     ###  11 12 16 18 21  
#         res = min(res, maxH - minH)                    ### 11 8 8 8 8
#     return res
# k = 3
# arr = [3, 9, 12, 16, 20]      ### 11
# k = 6
# arr = [12, 6, 4, 15, 17, 10]    ### 8
# ans = getMinDiff(arr, k)   
# print(ans)