#Author: Pedro Adrian Pereira
import math

def isPrime(n):
    maxDivisorCandidate = math.isqrt(n)
    prime = (n > 1)
    for d in range(2,maxDivisorCandidate+1):
        if (n % d == 0):
            prime = False
            break
    return prime
            
if __name__ == "__main__":
    n = int(input())
    ans = -1
    if (n - 2)%2 == 1 and isPrime(n - 2):
        ans = f"2 {n-2}"
    print(ans)