# Problem can be found at https://codeforces.com/problemset/problem/69/A

t = 0
A = B = C = 0
for i in range(int(input())):
          a,b,c = list(map(int,input().split(" ")))
          A = A + a
          B = B + b
          C = C + c
          if A == B == C == 0:
                    print("YES")
          else:
                    print("NO")
