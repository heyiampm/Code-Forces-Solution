# Problem can be found at https://codeforces.com/problemset/problem/448/A

a1,a2,a3 = map(int, input().split())
b1,b2,b3 = map(int, input().split())
n = int(input())

cups = a1 + a2 + a3
medals = b1 + b2 + b3

shelves_cups = (cups + 4) // 5      # ceil division
shelves_medals = (medals + 9) // 10 # ceil division

if shelves_cups + shelves_medals <= n:
          print("YES")
else:
          print("NO")