# Problem can be found at https://codeforces.com/problemset/submit


p, n = map(int, input().split())
m = {}

for i in range(n):
    x = int(input()) % p
    
    if x in m:
        print(i + 1)
        quit()
    m[x] = 1
        
print(-1)