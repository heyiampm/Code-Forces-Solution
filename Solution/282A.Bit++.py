#Problem name:("Bit++")//(Code forces problem 65)

x = 0
for i in range(int(input())):
    operation = input()
    if '+' in operation:
        x += 1
    else:
        x -= 1

print(x)
