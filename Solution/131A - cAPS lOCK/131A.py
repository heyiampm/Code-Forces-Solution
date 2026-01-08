# Problem can be found at https://codeforces.com/problemset/problem/131/A

t = input()
if t.isupper() or (len(t)==1) or t[1:].isupper():
          print(t.swapcase())
else:
          print(t)