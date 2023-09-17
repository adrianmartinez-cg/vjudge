def C2(n):
    return (n * (n - 1)) >> 1

n = int(input())
names = {}
x = 0
for _ in range(n):
    name = input()
    firstLetter = name[0]
    if firstLetter not in names:
        names[firstLetter] = 1
    else:
        names[firstLetter] += 1
for c in names:
    qt = names[c]
    numStudentsDiv2 = qt // 2
    numStudentsMod2 = qt % 2
    # uma das salas vai ter qt // 2 , e outra (qt // 2)+(qt%2)
    numCombRoom1 = C2(numStudentsDiv2)
    numCombRoom2 = C2(numStudentsDiv2+numStudentsMod2)
    x += numCombRoom1 + numCombRoom2
print(x)