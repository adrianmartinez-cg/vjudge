if __name__ == "__main__":
    t = int(input())
    ans = []
    for _ in range(t):
        nxinput = list(map(int,input().split()))
        n,x = nxinput[0],nxinput[1]
        A = list(map(lambda s : (int(s),1),input().split()))
        i = 0
        arrSum = 0
        while A[i][0]%x==0:
            A.append((A[i][0]//x, x*A[i][1]))
            i+=1
        for pair in A:
            arrSum += pair[0] * pair[1] 
        ans.append(arrSum)
    for answer in ans:
        print(answer)