#Problem name:("My First Sorting Problem")//(Code forces problem 09)

t = int(input())
for _ in range(t):
          x,y = (map(int, input().split()))
          print(min(x,y),max(x,y))