# Problem can be found at https://codeforces.com/problemset/problem/151/A

n, k, l, c, d, p, nl, np = map(int, input().split())
drink = (k * l) //nl
lime = c * d
salt = p // np
total = min(drink,lime,salt)
ans = total // n
print(ans)