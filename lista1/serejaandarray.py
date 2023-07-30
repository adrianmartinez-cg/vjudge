if __name__ == "__main__":
    nm = list(map(int,input().split()))
    n,m=nm[0],nm[1]
    A = list(map(int,input().split()))
    out = []
    accSum = 0
    for _ in range(m):
        entry = list(map(int,input().split()))
        op = entry[0]
        if op == 1:
            v = entry[1]
            x = entry[2]
            A[v-1] = x - accSum
        elif op == 2:
            y = entry[1]
            accSum += y
        elif op == 3:
            q = entry[1]
            out.append(A[q-1]+accSum)
    for val in out:
        print(val)