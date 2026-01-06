# Problem can be found at https://codeforces.com/problemset/problem/41/A

s = input().strip()
t = input().strip()
if s[::-1] == t:
       print("YES")
else:
       print("NO")
