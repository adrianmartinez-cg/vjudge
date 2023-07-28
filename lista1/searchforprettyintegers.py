
def minValueInCommon(A,B):
    setA = set(A)
    setB = set(B)
    intersect = setA.intersection(setB)
    if len(intersect) > 0:
        return min(intersect)
    else:
        return 90 # o valor máximo obtido por concatenação seria 89

# Author: Pedro Adrian Pereira Martinez
if __name__ == "__main__":
    nm = list(map(int,input().split()))
    n,m = nm[0],nm[1]
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    j,k = A[n-1],B[m-1]
    candidate1 = int(f"{min(j,k)}{max(j,k)}")
    candidate2 = minValueInCommon(A,B)
    print(min(candidate1,candidate2))
