import math

num = int(input("Enter a Number to finds it's factors : "))

# Brute force Approach - Time : O(n)
count1 = 0
for i in range(1,num+1):
  if num % i == 0:
    count1 += 1

print("Brute force ")
print(f"No of Factors of {num} are : ",count1)


# Optimial Approach - Time : O(√n)
count2 = 0
for i in range(1,int(math.sqrt(num))+1):
  if num % i == 0:
    if i == (num//i):
      count2 += 1       # Perfect Square
    else:
      count2 += 2      # Both i and (n / i) are factors of num
    
print("Optimial")
print(f"No of Factors of {num} are : ",count2)