# Problem can be found at https://codeforces.com/problemset/problem/272/A

n = int(input())
t = sum(list(map(int, input().split())))
pm = 0
for i in range(1, 6):
    if (t + i) % (n + 1) != 1:
        pm += 1
print(pm)