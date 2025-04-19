import math

def partial_permutations(n, k):
    result = math.factorial(n) // math.factorial(n - k)
    return result % 1_000_000

# Sample input
n = 21
k = 7

# Output
print(partial_permutations(n, k))
