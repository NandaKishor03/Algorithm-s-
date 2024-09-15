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
