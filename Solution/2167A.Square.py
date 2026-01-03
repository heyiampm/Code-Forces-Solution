#Problem name:("Square")//(Code forces problem 03)

t = int(input())
for _ in range(t):
          sticks = list(map(int, input().split()))
          if sticks.count(sticks[0]) == 4:
                    print("Yes")
          else:
                    print("NO")