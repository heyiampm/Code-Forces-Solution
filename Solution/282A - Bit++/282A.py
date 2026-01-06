# Problem can be found at https://codeforces.com/problemset/problem/282/A

x = 0
for i in range(int(input())):
    operation = input()
    if '+' in operation:
        x += 1
    else:
        x -= 1

print(x)
