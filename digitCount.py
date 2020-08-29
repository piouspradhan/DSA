import math
import time

N = int(input("Enter Number: "))
M = N
#Method 1
#Time Complexity = O(digitCount) or O(n)
start_time = time.time()
digitCount = 0

while N != 0:
    digitCount += 1
    N = int(N/10)

print("Number of digits:",digitCount)
print("--- %s seconds ---" % (time.time() - start_time))

#Method2
#Time Complexity = O(1)
start_time = time.time()
digCount = 1 + int(math.log10(M))
print("Number of digits:",digCount)
print("--- %s seconds ---" % (time.time() - start_time))
