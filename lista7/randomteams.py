def C2(n):
    return (n * (n - 1)) >> 1

n,m = list(map(int,input().split()))
maxFriends = C2(n-(m-1))
if m == 1:
    print(f"{maxFriends} {maxFriends}")
else:
    # para o pior caso : n%m grupos com (n//m + 1) participantes, (m-n%m) grupos com n//m participantes
    q = n // m
    rm = n % m
    numFriends1 = rm * C2(q+1)
    numFriends2 = (m-rm) * C2(q)
    minFriends = numFriends1 + numFriends2
    print(f"{minFriends} {maxFriends}") 