# Problem can be found at https://codeforces.com/problemset/problem/1977/A

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n >= m and (n - m) % 2 == 0:
        print("Yes")
    else:
        print("No")
