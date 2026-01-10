# Problem can be found at https://codeforces.com/problemset/problem/469/A

n = int(input())
levels = set()
for _ in range(2):
    a = list(map(int, input().split()))
    levels |= set(a[1:])
print("I become the guy." if len(levels) == n else "Oh, my keyboard!")
