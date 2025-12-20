# #Problem name:("Submission Bait")//(Code forces problem 15)

t = int(input())
from collections import Counter

for _ in range(t):
          n = int(input())
          a = list(map(int, input().split()))
          c = Counter(a)
          ok = False
          
          for v in c.values():
                    if v % 2 == 1:
                              ok = True
                              break
          print("YES" if ok else "NO")
