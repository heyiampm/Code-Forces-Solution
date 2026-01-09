# Problem can be found at https://codeforces.com/problemset/problem/2179/A

t = int(input())
for _ in range(t):
    k, x = map(int, input().split())
    print(k * x + 1)
