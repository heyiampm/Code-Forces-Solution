#Problem name:("Buttons")//(Code forces problem 26)

t = int(input())
for _ in range(t):
          a,b,c = map(int,input().split())
          if a > b :
                    print("First")
          elif a < b:
                    print("Second")
          else:
                    if c% 2 == 1:
                              print("First")
                    else:
                              print("Second")
