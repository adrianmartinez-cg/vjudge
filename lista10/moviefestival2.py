import heapq

n,k = map(int,input().split())
movies = []
for i in range(n):
    a,b = map(int,input().split())
    movies.append((b,a,i))
movies.sort(reverse=True)
busy = []
cantWatch = 0
while movies:
    movie = movies.pop()
    end,start,id = movie
    numBusy = len(busy)
    if numBusy < k:
        heapq.heappush(busy,(end,id))
    else:
        fMovieEnd,fMovieId = heapq.heappop(busy)
        if start >= fMovieEnd:
            heapq.heappush(busy,(end,id))
        else:
            heapq.heappush(busy,(fMovieEnd,fMovieId))
            cantWatch += 1
print(n-cantWatch)