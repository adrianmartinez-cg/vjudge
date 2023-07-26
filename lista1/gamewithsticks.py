input = list(map(int,input().split()))
n,m = input[0],input[1]
i,j = n,m # numero de linhas horizontais e verticais em uma iteração
intersectPoints = i * j
turn = 0
while (intersectPoints > 0):
    intersectPoints -= (i+j-1)
    i-=1
    j-=1
    turn += 1
if(turn % 2 == 0):
    print('Malvika')
else:
    print('Akshat')