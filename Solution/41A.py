#Problem name:("Translation")//(Code forces problem 36)

s = input().strip()
t = input().strip()
if s[::-1] == t:
       print("YES")
else:
       print("NO")
