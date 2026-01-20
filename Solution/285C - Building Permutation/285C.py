
n = int(input())
l_i = list(map(int, input().split()))
l_i.sort()

c = 1
t = 0
for i in l_i:
    t += abs(c - i)
    c += 1
print(t)
    