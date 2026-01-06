# Problem can be found at https://codeforces.com/problemset/problem/467/A

r = 0
for _ in range(int(input())):
    p, q = map(int, input().split())
    if q - p >= 2:
        r += 1

print(r)
