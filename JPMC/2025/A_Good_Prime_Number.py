# Problem Statement  :

# A prime number is a number which is divisible by one and itself. Also a number is called a good  prime number if the sum of its digits is a prime number. For example a number 23 is a good prime number because the sum of 2 and 3 ( 2+3=5) is 5 which is a prime number. You are given an integer K. Your task is to find the kth good prime number that is greater than a provided number N.

# For example , 232 is a good prime number since the sum of all digits is 7 which is a prime number whereas 235 is not a good prime number.

# Input format :

# The first line contains an integer N.
# The next line contains an integer K.
# Output format :

# A single integer which is a Kth good prime number that is greater than a provided number N.

# Constraints :
# 1<=N<=10^5
# 1<=K<<=10^5

# Sample Input 1:
# 4  4

# Sample Output 1:
# 12

def isprime(n):
  if n == 1:
    return False
  elif n <= 3:
    return True
  elif n % 2 == 0 or n % 3 == 0:
    return False
  else:
    for i in range(5,int(n**0.5)+1,6):
      if n%i == 0 or n%(i+2) == 0:
        return False
  return True


def solve(num,k):
  count = 0
  # lst = []
  for i in range(num+1,1000000):
    temp = i
    sum = 0
    while temp != 0:
      sum = sum + temp % 10
      temp //= 10
    if isprime(sum):
      # lst.append(i)
      res = i
      count += 1
    if count == k:
      break
  # print(lst)
  # return lst[k-1]
  return res

num = int(input())
k = int(input())
print(solve(num,k))
