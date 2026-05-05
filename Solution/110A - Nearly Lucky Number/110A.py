# Problem can be found at https://codeforces.com/problemset/problem/110/A

n = input()
count = 0
for digit in n:
    if digit == '4' or digit == '7':
        count += 1
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")