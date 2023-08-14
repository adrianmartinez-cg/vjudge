n = int(input())
st = set()
for _ in range(n):
    s = input()
    rs = s[::-1]
    if (s not in st) and (rs not in st):
        st.add(s)
print(len(st))