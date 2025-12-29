# Problem Name ("Carnival Wheel")

import math
t = int(input())
for _ in range(t):
    l, a, b = map(int, input().split())
    g = math.gcd(l, b)
    print(l - g + a % g)