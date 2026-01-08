# Problem can be found at https://codeforces.com/problemset/problem/336/B

n, k = map(int, input().split())
h = list(map(int, input().split()))

cur = sum(h[:k])
min_sum = cur
idx = 1

for i in range(k, n):
          cur += h[i] - h[i - k]
          if cur < min_sum:
                    min_sum = cur
                    idx = i - k + 2

print(idx)