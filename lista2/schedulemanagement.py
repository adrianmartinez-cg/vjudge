def getNumTasks(a,n):
    numTasks = {}
    for i in range(1,n+1):
        numTasks[i] = 0
    for task in a:
        numTasks[task] += 1
    return numTasks

def allDone(m,h,numTasks):
    tasksLeft = m
    extraTasks = 0
    for i in numTasks:
        tasksToDo = numTasks[i]
        if h >= tasksToDo:
            tasksLeft -= tasksToDo
            extraTasks += (h - tasksToDo) // 2
        else:
            tasksLeft -= h
    tasksLeft -= extraTasks
    if tasksLeft > 0:
        return False
    else:
        return True
        
def binarySearch(m,l,r,h,numTasks):
    if l > r:
        return h
    mid = (l+r)//2
    isDone = allDone(m,mid,numTasks)
    if not isDone:
        return binarySearch(m,mid+1,r,h,numTasks)
    elif isDone:
        return binarySearch(m,l,mid-1,mid,numTasks)

t = int(input())
ans = []
for _ in range(t):
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    numTasks = getNumTasks(a,n)
    ans.append(binarySearch(m,1,2*m,2*m,numTasks))
for _ in ans:
    print(_)