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
# grid_x , grid_y = 3 , 3
# ins = ['R','M','L','M','L','M']
# # grid_x , grid_y = 3 , 4
# # ins = ['R','M','L','M','L','M','R','M']
# x , y , facing = 2 , 2 , 'E'
# output_string = ""
# def next_facing(curr_facing , move):
#     directions = {'N':['W','E'] , 'S' :['E' , 'W'] , 'W' : ['S', 'N'] , 'E' : ['N' , 'S']}
#     if move == 'R':
#         return directions.get(curr_face)[1]
#     else:
#         return directions.get(curr_face)[0]
# curr_x , curr_y , curr_face = x , y , facing
# for x in ins:
#     if x == 'R' or x == 'L':
#         curr_face = next_facing(curr_face , x)
#         continue
#     elif x == 'M':
#         if curr_face == 'N':
#             i , j = 0 , 1
#         elif curr_face == 'E':
#             i , j = 1, 0
#         elif curr_face == 'S':
#             i , j = 0, -1
#         elif curr_face == 'W':
#             i , j = -1 , 0
#         if (curr_x + i) > grid_x or (curr_y + j ) > grid_y or (curr_x + i ) <= 0 or (curr_y + j) <= 0 :
#             # print(str(curr_x)+'-'+str(curr_y)+'-'+str(curr_face)+'-ER')
#             output_string += "-ER"
#             break
#         curr_x = curr_x + i
#         curr_y = curr_y + j
# print(str(curr_x)+'-'+str(curr_y)+'-'+str(curr_face) + output_string)



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



### Maximum Negative Sequence length and Return sum
### If the length of two Sequence sum is Same than add the Sum of Two Sequence
# arr = [15,-3,-4,-19,-20,24,5,-7,-3,-38,0,16,18,-2]
# arr = [15,-4,-19,-20,24,5,-7,-3,-38,0,16,18,-2]
# arr = [15,-4,-19,-20,24,5,-7,-3,-38,0,16,18,1,5,-3,-15,-1,20]
# arr = [15,-4,-19,-20,24,5,-7,-3,-38,0,16,18,1,5,20,-3,-15,-1]
# dct = {}
# count = 0
# length = 0
# arr_length = 0
# for x in arr:
#     arr_length += 1
#     if x >= 0 :
#         dct[count] = length
#         count = 0
#         length = 0
#     else:
#         count += x
#         length += 1
#     if arr_length == len(arr) and count != 0 :
#         dct[count] = length
# sorted_lst = sorted(dct.items() , key=lambda x: -x[1])
# length = sorted_lst[0][1]
# res = sorted_lst[0][0]
# for i in range(1,len(sorted_lst)):
#     if length == sorted_lst[i][1]:
#         res += sorted_lst[i][0]
#         # length += length
# if res == 0:
#     print(sorted_lst[0][0])
# else:
#     print(res)



# ### User Password Generator
# ### Based on First_Name , Last_Name , Pin_Code , Position (N)
# # first_name , last_name , pin , N = 'Rajiv' , 'Roy' , 560037 , 6
# # first_name , last_name , pin , N = 'Manoj' , 'Kumar' , 561327 , 2
# first_name , last_name , pin , N = 'Kumud' , 'Kumar' , 561327 , 2
# result = ""
# if len(first_name) < len(last_name):
#     smaller = first_name[-1].upper()
#     longer = last_name.swapcase()
#     result += smaller
#     result += longer
# elif len(last_name) < len(first_name):
#     smaller = last_name[-1].upper()
#     longer = first_name.swapcase()
#     result += smaller
#     result += longer
# else:
#     n = len(first_name)
#     for i in range(n):
#         if ord(first_name[i]) < ord(last_name[i]):
#             smaller = first_name[-1].upper()
#             longer = last_name.swapcase()
#             result += smaller
#             result += longer
#             break
#         else:
#             smaller = last_name[-1].upper()
#             longer = first_name.swapcase()
#             result += smaller
#             result += longer
#             break
# pin = str(pin)
# LR , RL = pin[N-1] , pin[-N]
# result += LR
# result += RL
# print(result)



###  Job schedulling based on the max profit with the slot time and return the N job's in the order
# # arr = [['j1' , 1 , 60],
# #        ['j2' , 2 , 100],
# #        ['j3' , 3 , 20],
# #        ['j4' , 2 , 40],
# #        ['j5' , 1 , 20]]             ### Output : ['j1' , 'j2' , 'j3'] , profit = 180
# arr = [['j1' , 2 , 100],
#        ['j2' , 2 , 50],
#        ['j3' , 1 , 25],
#        ['j4' , 1 , 19],
#        ['j5' , 3 , 20]]           ### Output : ['j2', 'j1', 'j5'] , profit = 170
# n = 3
# for i in range(len(arr)):
#     for j in range(n-1-i):
#         if (arr[j][2] < arr[j+1][2]):
#             arr[j] , arr[j+1] = arr[j+1] , arr[j]
# result = [False] * n
# job = [-1] * n
# profit = 0
# for i in range(len(arr)):
#     for j in range(min(n-1,arr[i][1]-1),-1,-1):
#         if (result[j] is False):
#             result[j] = True
#             job[j] = arr[i][0]
#             profit += arr[i][2]
#             break
#     print(result)
#     print(job)
# print("Profit : ",profit)




### Calculate the Minimum No.of terms in the Fibonacci Series to get the number k
def CalcFibonacciSeries(FiboTerm , K):
    i = 3
    FiboTerm.append(0)
    FiboTerm.append(1)
    FiboTerm.append(1)
    while True:
        nextTerm = (FiboTerm[i-1] + FiboTerm[i-2])
        if nextTerm > K:
            return
        FiboTerm.append(nextTerm)
        i += 1
    
## To get Minimum no.of terms travesre the fibonacci series upto k in the from end
def findMinTerms(K):
    k = K
    FiboTerm = []
    CalcFibonacciSeries(FiboTerm , K)
    count , j =  0 , len(FiboTerm) - 1
    while K > 0:
        count += K // FiboTerm[j]
        K %= FiboTerm[j]
        j-=1
    print("Minimum no of terms to get ",k,'are : ',count)

## To get Maximum no.of terms travesre the fibonacci series upto k in the from front
# Maximum CROSS CHECK
# def findMaxTerms(K):
#     k = K
#     FiboTerm = []
#     CalcFibonacciSeries(FiboTerm , K)
#     count , i =  0 , 1
#     while K > 0:
#         count += K // FiboTerm[i]
#         K %= FiboTerm[i]
#         i-=1
#     print("Minimum no of terms to get ",k,'are : ',count)

findMinTerms(10)
# findMaxTerms(10)




