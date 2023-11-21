def minValueInCommon(A,B):
    setA = set(A)
    setB = set(B)
    intersect = setA.intersection(setB)
    if len(intersect) > 0:
        return min(intersect)
    else:
        return 90 # o valor máximo obtido por concatenação seria 89

n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
j,k = A[0],B[0]
candidate1 = int(f"{min(j,k)}{max(j,k)}")
candidate2 = minValueInCommon(A,B)
print(min(candidate1,candidate2))