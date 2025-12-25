#Problem name:("LOL Lovers")//(Code forces problem 38)

n = int(input())
s = input()

for k in range(1, n):
    mine = s[:k]
    theirs = s[k:]
    if mine.count('L') != theirs.count('L') and mine.count('O') != theirs.count('O'):
        print(k)
        exit()

print("-1")