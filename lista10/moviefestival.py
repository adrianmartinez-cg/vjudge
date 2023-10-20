n = int(input())
movies = []
maxMovies = 1
for _ in range(n):
    a,b = map(int,input().split())
    movies.append((b,a))
movies.sort(reverse=True)
movie = movies.pop()
end = movie[0]
while movies:
    if movies[len(movies)-1][1] < end:
        movies.pop()
    else:
        movie = movies.pop()
        end = movie[0]
        maxMovies += 1
print(maxMovies)