# Author: Pedro Adrian Pereira Martinez
if __name__ == "__main__":
    inputArr = list(map(int,input().split()))
    power = 0
    ans = 0
    for num in inputArr:
        if(num):
            ans += 2**power
        power += 1
    print(ans)