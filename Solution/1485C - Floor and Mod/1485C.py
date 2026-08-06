import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    ans = 0
    b = 1

    while b <= y:
        k = x // (b + 1)
        if k == 0:
            break

        last = min(y, x // k - 1)

        split = k + 1

        # First part: arithmetic progression
        r1 = min(last, split)
        if b <= r1:
            n = r1 - b + 1
            ans += ((b - 1) + (r1 - 1)) * n // 2

        # Second part: constant k
        l2 = max(b, split + 1)
        if l2 <= last:
            n = last - l2 + 1
            ans += n * k

        b = last + 1

    print(ans)