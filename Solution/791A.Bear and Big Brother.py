#Problem name:("Bear and Big Brother")//(Code forces problem 72)

a, b = map(int, input().split())

c = 0
while a <= b:
    a = a * 3
    b = b * 2
    c += 1

print(c)
