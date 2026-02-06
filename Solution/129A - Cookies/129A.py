# Problem can be found at https://codeforces.com/problemset/problem/129/A

n = int(input())

l_b = list(map(int, input().split()))
s_b = sum(l_b)
t = 0
 
for b in l_b:
    if (s_b - b) % 2 == 0:
        t += 1
 
print(t)