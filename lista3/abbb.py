t = int(input())
ans = []
for _ in range(t):
    st = []
    s = input()
    for c in s:
        if c == "A":
            st.append(c)
        elif c == "B":
            if len(st) > 0:
                st.pop()
            else:
                st.append(c)
    ans.append(len(st))
for _ in ans:
    print(_)