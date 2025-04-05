import math

numbers = list(map(int,input("Enter a list Numbers to finds it's factors of each number : ").split(" ")))

# Brute Force Approach - time : O()
def count_factors_optimal(num):
    count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if i == num // i:
                count += 1
            else:
                count += 2
    return count

print("\nResults:\n")

for num in numbers:
    optimal = count_factors_optimal(num)
    print(f"Number: {num}")
    print(f"  Optimal count    : {optimal}\n")



# Optimial Approach (Sieve of Eratosthenes) - Time : O(nlog(n))
def count_factors_optimal(num):
  factor_count = [0] * (num + 1)
  for i in range(1 , num + 1):
    for j in range(i , num + 1 , i):
      factor_count[j] += 1

  return factor_count

lst = {}
for num in numbers:
  optimal = count_factors_optimal(num)
  lst[num] = optimal[-1]

print("Optimial")
print("List of Factors of Numbers : ",lst)


# Example for Better Understanding:
# Let's say n = 6.

# We initialize: factor_count = [0, 0, 0, 0, 0, 0, 0]

# Now we go through:

# i = 1: increments factor_count[1 to 6] by 1 → all numbers are divisible by 1
# → [0, 1, 1, 1, 1, 1, 1]

# i = 2: increments 2, 4, 6
# → [0, 1, 2, 1, 2, 1, 2]

# i = 3: increments 3, 6
# → [0, 1, 2, 2, 2, 1, 3]

# i = 4: increments 4
# → [0, 1, 2, 2, 3, 1, 3]

# i = 5: increments 5
# → [0, 1, 2, 2, 3, 2, 3]

# i = 6: increments 6
# → [0, 1, 2, 2, 3, 2, 4]

# So:

# 1 has 1 factor

# 2 has 2 factors → (1, 2)

# 3 has 2 factors → (1, 3)

# 4 has 3 factors → (1, 2, 4)

# 5 has 2 factors → (1, 5)

# 6 has 4 factors → (1, 2, 3, 6)

# 💡 Why is it Efficient?
# Instead of checking each number individually (which takes O(√n) time per number), we flip the process:

# Each number i marks itself as a factor for all its multiples.

# The outer loop runs n times.

# The inner loop runs n/i times for each i, so total work is approximately:

# n/1 + n/2 + n/3 + ... + n/n = O(n log n)

# Much better than O(n√n) if you're checking each number with the optimal approach one by one.