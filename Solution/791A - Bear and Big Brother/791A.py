# Problem can be found at https://codeforces.com/problemset/problem/791/A

a, b = map(int, input().split())

c = 0
while a <= b:
    a = a * 3
    b = b * 2
    c += 1

print(c)
