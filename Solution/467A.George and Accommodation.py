#Problem name:("George and Accommodation")//(Code forces problem 66)

r = 0
for _ in range(int(input())):
    p, q = map(int, input().split())
    if q - p >= 2:
        r += 1

print(r)
