import math

num = int(input("\nEnter a Number: "))

# Optimial Approach - Time : O(√n)
def Check_Prime(n):
    if n <= 1:
        print("Not a Prime")
        return
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            print("Not a Prime")
            return
    print("Prime")



# Number Prime Number upto n

# Burte Force Approach - Time : O(n^2)
def Burte_Prime_number(num):
  primes = []
  for i in range(2,num+1):
    is_prime = True
    for j in range(2,i):
      if i % j == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(i)

  print(f"\nNumber of primes up to {num}: {len(primes)}")
  print(primes)




# Optimial Approach 2 (Sieve of Eratosthenes) - Time : O(nlog(log(n))) -> Very Fast -> Almost Linear
def Optimal_Prime_number(num):
  prime = [True] * (num+1)
  prime[0] = prime[1] = False

  for i in range(2,num+1):
    if prime[i]:
      for j in range(i*i , num+1 , i):
        prime[j] = False

  primes = [i for i in range(num + 1) if prime[i]]
  prime_count = sum(1 for i in range(num+1) if prime[i])
  print(f"\nNumber of primes up to {num}: {prime_count}")
  print(primes)

Check_Prime(num)
Burte_Prime_number(num)
Optimal_Prime_number(num)


print("Prime Numbers")