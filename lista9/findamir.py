n = int(input())
if n % 2 == 0:
    minCost = (n // 2) - 1
else:
    minCost = (n - 1) // 2
print(minCost)