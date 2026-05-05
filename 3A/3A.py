s, t = input(), input()
x, y = ord(s[0]), int(s[1])
a, b = ord(t[0]), int(t[1])
r = []

while (x, y) != (a, b):
    m = ''
    # row movement
    if y < b:
        y += 1
        m += 'U'
    elif y > b:
        y -= 1
        m += 'D'
    # column movement
    if x < a:
        x += 1
        m += 'R'
    elif x > a:
        x -= 1
        m += 'L'

    r.append(m)

print(len(r))
print(*r, sep='\n')