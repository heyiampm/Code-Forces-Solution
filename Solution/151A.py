#Problem name:("Soft Drinking")//(Code forces problem 31)

n, k, l, c, d, p, nl, np = map(int, input().split())
drink = (k*l)//nl
lime = c*d
salt = p//np
total = min(drink,lime,salt)
ans = total //n
print(ans)

