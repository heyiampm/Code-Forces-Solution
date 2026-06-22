import sys
input = sys.stdin.readline

def solve(n):
    result = [0] * (4 * n)
    
    for x in range(1, n + 1):
        p1 = x - 1
        p2 = n + 2 * (x - 1)
        p3 = n + 2 * (x - 1) + 1
        p4 = 3 * n + (x - 1)
        result[p1] = result[p2] = result[p3] = result[p4] = x
    if n % 2 == 1:
        xc = (n + 1) // 2
        p3_xc  = n + 2 * (xc - 1) + 1
        p2_xp1 = n + 2 * xc
        result[p3_xc], result[p2_xp1] = result[p2_xp1], result[p3_xc]
    
    print(*result)

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)