#Problem name:("Even Odds")//(Code forces problem 44)

n, k = map(int, input().split())
odds_count = (n + 1) // 2 
if k <= odds_count:
    result = 2 * k - 1
else:
    result = (k - odds_count) * 2
print(int(result))
