#Problem name:("Your Name")//(Code forces problem 02)

q = int (input())
for _ in range(q):
          n = int(input())
          s , t = input().split()
          if sorted(s) == sorted(t):
                    print("YES")
          else:
                    print("NO")