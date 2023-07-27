def func(x):
    numStr = str(x)
    n = len(numStr)
    digit = numStr[n-1]
    result = ""
    for i in range(n-1,-1,-1):
        if numStr[i] != 0:
            result += numStr[i]
    return result
