def checkLetters(str,letters):
    left = 0
    right = len(str) - 1
    while left <= right:
        if str[left] in letters:
            letters[str[left]] += 1
        else:
            letters[str[left]] = 1
        if left < right:
            if str[right] in letters:
                letters[str[right]] += 1
            else:
                letters[str[right]] = 1
        left += 1
        right -= 1

s = input()
t = input()
lettersT = {}
checkLetters(t,lettersT)
matchCL = 0
matchL = 0
for char in s:
    if char not in lettersT:
        lettersT[char.swapcase()] -= 1
        matchL += 1
    elif lettersT[char] > 0:
        lettersT[char] -= 1
        matchCL += 1
    else:
        lettersT[char.swapcase()] -= 1
        matchL += 1
print(f"{matchCL} {matchL}")