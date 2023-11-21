def isPalindrome(s):
    return s[::] == s[::-1]

s = input()
longest = 1
for i in range(len(s)):
    actual = s[i]
    for j in range(i+1,len(s)):
        actual += s[j]
        if isPalindrome(actual):
            if len(actual) > longest:
                longest = len(actual)
print(longest)