# Problem can be found at https://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
scores = list(map(int, input().split()))

# cutoff = score at k-th place (1-indexed so k-1 in Python)
cutoff = scores[k-1]

count = 0
for score in scores:
    if score >= cutoff and score > 0:
        count += 1

print(count)