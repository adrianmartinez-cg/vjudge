def accSum(A):
    for i in range(2,len(A)):
        A[i] += A[i-1]

n = int(input())
A = [0] * (n+1)
for _ in range(n):
    a,b = map(int,input().split())
    A[a] += 1
    if b + 1 <= n:
        A[b+1] -= 1
accSum(A)
print(max(A))