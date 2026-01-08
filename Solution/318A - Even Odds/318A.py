# Problem can be found at https://codeforces.com/problemset/problem/381/A

n, k = map(int, input().split())
odds_count = (n + 1) // 2 
if k <= odds_count:
    ans = 2 * k - 1
else:
    ans = (k - odds_count) * 2
print(int(ans)) 