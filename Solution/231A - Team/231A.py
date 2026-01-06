# Problem can be found at https://codeforces.com/problemset/problem/231/A
a = int(input())
tcount = 0

for i in range(a):
    j = input().split()
    count = 0

    for k in j:
        if k == "1":
            count += 1
    
    if count >= 2:
        tcount += 1

print(tcount)