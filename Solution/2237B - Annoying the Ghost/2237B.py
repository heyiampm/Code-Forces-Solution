import sys
from bisect import bisect_left
input = sys.stdin.readline
def merge_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, lc = merge_count(arr[:mid])
    right, rc = merge_count(arr[mid:])
    merged = []
    count = lc + rc
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    pairs = sorted(zip(b, range(n)))
    active_vals = [p[0] for p in pairs]
    active_idxs = [p[1] for p in pairs]

    perm = []
    possible = True

    for i in range(n):
        pos = bisect_left(active_vals, a[i])
        if pos == len(active_vals):
            possible = False
            break
        perm.append(active_idxs[pos])
        active_vals.pop(pos)
        active_idxs.pop(pos)

    if not possible:
        print(-1)
        return

    _, ans = merge_count(perm)
    print(ans)

t = int(input())
for _ in range(t):
    solve()