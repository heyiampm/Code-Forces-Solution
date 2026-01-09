# Problem can be found at https://codeforces.com/problemset/problem/2180/A

import math
t = int(input())
for _ in range(t):
    l, a, b = map(int, input().split())
    g = math.gcd(l, b)
    print(l - g + a % g)