# Dada a sequência 1,1,2,1,2,3,1,2,3,4(...) retorna o k-ésimo termo
# A sequencia é construida por "somas", onde cada soma é a soma dos n-primeiros naturais
def findKthElemSeq(k):
    n = 0 
    S = 0
    while S < k:
        n += 1 
        S = n*(n+1)//2
    if S > k:
        S = (n-1)*(n) // 2
    if S == k:
        return n
    else:
        return k - S

# Author: Pedro Adrian Pereira Martinez
if __name__ == "__main__":
    nk = list(map(int,input().split()))
    n,k = nk[0],nk[1]
    A = list(map(int,input().split()))
    print(A[findKthElemSeq(k)-1])
