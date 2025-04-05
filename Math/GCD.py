# gcd(a, b) = gcd(a, b - a)     # Classical Euclidean Algorithm
# gcd(a, b) = gcd(b % a, a)     # Optimized Euclidean Algorithm


def gcd_c(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print("Classical GCD:", a)


def gcd_o(a, b):
    while a != 0:
        a, b = b % a, a
    print("Optimized GCD:", b)

a, b = map(int, input("Enter two numbers to find GCD: ").split())
gcd_c(a, b)
gcd_o(a, b)