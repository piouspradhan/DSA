import time

N = int(input("Enter number: "))

## Method1: Classical Sieve of Eratosthenes
## Time Complexity: O(n*log(log(n)))
start_time = time.time()
prime = [True for i in range(N+1)]
p = 2
while (p*p < N+1):
    if prime[p]:
        for i in range(p*p, N+1, p):
            prime[i] = False
    p += 1

prime_num = []
for j in range(2, N+1):
    if prime[j]:
        prime_num.append(j)

print(prime_num)
print("--- %s seconds ---" % (time.time() - start_time))
