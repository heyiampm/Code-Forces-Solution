#Problem name:("Word")//(Code forces problem 68)

s = input()

u = 0
l = 0

for i in s:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1

if u > l:
    print(s.upper())
else:
    print(s.lower())
