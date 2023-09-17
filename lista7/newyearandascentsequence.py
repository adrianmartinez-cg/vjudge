# incompleto
def isAscent(seq):
    existsAscent = False
    for i in range(2,len(seq)-1):
        diff = seq[i] - seq[i-1]
        if diff > 0:
            existsAscent = True
            break
    return existsAscent

def findMinMax(seq):
    minNumber = 10**6 + 1
    maxNumber = -1
    for i in range(1,len(seq)):
        if seq[i] > maxNumber:
            maxNumber = seq[i]
        if seq[i] < minNumber:
            minNumber = seq[i]
    return minNumber,maxNumber

def binarySearch(l, r, x, seq):
    # modificado para retornar o valor mais a esquerda , em caso de numeros repetidos
    result = -1
    repeat = False  
    while l <= r:
        mid = (l + r) // 2
        e = seq[mid]
        if e == x:
            result = mid 
            r = mid - 1   
        elif e < x:
            l = mid + 1
        else:
            r = mid - 1
    return result

n = int(input())
numConcat = n * n
minInSeq = []
maxInSeq = []
count = 0
for i in range(n):
    seq = list(map(int,input().split()))
    if not isAscent(seq):
        minNumber,maxNumber = findMinMax(seq)
        minInSeq.append(minNumber) 
        maxInSeq.append(maxNumber)
maxInSeq.sort()
for m in minInSeq:
    elemsBefore = binarySearch(0,len(maxInSeq)-1,m,maxInSeq)
    count += elemsBefore
feasible = numConcat - count
print(feasible)