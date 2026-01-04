#Problem name:("Young Physicist")//(Code forces problem 69)

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
