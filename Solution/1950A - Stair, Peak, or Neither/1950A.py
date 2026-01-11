# Problem can be found at https://codeforces.com/problemset/problem/1950/A

t = int(input())
for _ in range(t):
          a,b,c = map(int, input().split())
          
          if a<b<c:
                    print("STAIR")
          elif a<b>c:
                    print("PEAK")
          else:
                    print("NONE")