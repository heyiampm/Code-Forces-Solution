#Problem name:("Sereja and Dima")//(Code forces problem 49)

n = int(input())
a = list(map(int, input().split()))
s = d = 0
while a:
          s += a.pop(0) if a[0] > a[-1] else a.pop()
          if a:
                    d += a.pop(0) if a[0] > a[-1] else a.pop()
print(s, d)
