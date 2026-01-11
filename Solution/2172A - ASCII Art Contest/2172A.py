# Problem can be found at https://codeforces.com/problemset/problem/2172/A

g, c, l = map(int, input().split())
if not (80 <= g <= 100 and 80 <= c <= 100 and 80 <= l <= 100):
          print("check again")
          
elif max(g, c, l) - min(g, c, l) >= 10:
          print("check again")
          
else:
          print("final", g + c + l - max(g, c, l) - min(g, c, l))