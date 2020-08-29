import time

## GCD using Basic Euclidean Method
## Time Complexity: O(min(a,b))

def gcd(a,b):
    if a == 0:
        return b

    return gcd(b%a, a)

n = input("Enter numbers: ").split()

print(gcd(int(n[0]), int(n[1])))
