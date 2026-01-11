# Problem can be found at https://codeforces.com/problemset/problem/1912/L

n = int(input())
s = input()
for k in range(1, n):
    mine = s[:k]
    theirs = s[k:]
    if mine.count('L') != theirs.count('L') and mine.count('O') != theirs.count('O'):
        print(k)
        exit()

print("-1")