import math

len = int(input())

result = 0

isPrime = True

for i in range(2, len + 1):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        result += i
    else:
        isPrime = True
print(result)
