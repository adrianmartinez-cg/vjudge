# Author: Pedro Adrian Pereira Martinez
if __name__ == "__main__":
    t = int(input())
    ans = []
    for _ in range(t):
        n = input()
        ans.append(len(n))
    for answer in ans:
        print(answer)