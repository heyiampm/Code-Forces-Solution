# Problem can be found at https://codeforces.com/problemset/problem/1472/A

for _ in range(int(input())):
    w, h, n=map(int, input().split())
    c = 1
    while w %2 == 0: w //=2; c *= 2
    while h % 2== 0: h //=2; c *= 2
    print("YES" if c>=n else "NO")