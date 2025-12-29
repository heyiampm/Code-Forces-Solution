# Problem Name ("Yes Or Yes")

t = int(input())
for _ in range(t):
    s = input().strip()
    if s[0] == 'Y' and s[-1] == 'Y':
        print("NO")
    else:
        print("YES")