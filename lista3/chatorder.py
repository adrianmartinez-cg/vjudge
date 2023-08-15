n = int(input())
stk = []
pos = {}
for i in range(n):
    f = input()
    stk.append(f)
    pos[f] = i
ans = []
for i in range(n):
    if pos[stk[i]] == i:
        ans.append(stk[i])
for i in range(len(ans)-1,-1,-1):
    print(ans[i])