def countOnes(A,n):
    count = 0
    for i in range(n):
        if A[i] == 1:
            count += 1
    return count

# Author: Pedro Adrian Pereira
if __name__ == "__main__":
    inputStr = list(map(int,input().split()))
    n,q = inputStr[0],inputStr[1]
    A = list(map(int,input().split()))
    ones = countOnes(A,n)
    ans = []
    for _ in range(q):
        query = list(map(int,input().split()))
        op = query[0]
        if op == 1:
            x = query[1]
            if A[x-1] == 0:
                ones += 1
            else:
                ones -= 1
            A[x-1] = 1 - A[x-1]
        elif op == 2:
            k = query[1]
            if k <= ones:
                ans.append(1)
            else:
                ans.append(0)
    for answer in ans:
        print(answer)