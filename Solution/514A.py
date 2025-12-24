#Problem name:("Chewbaсca and Number")//(Code forces problem 34)

s = list(input().strip())
for i in range(len(s)):
    d = int(s[i])
    if i == 0 and s[i] == '9':
        continue
    if 9 - d < d:
        s[i] = str(9 - d)
print("".join(s))