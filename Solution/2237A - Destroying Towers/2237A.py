t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = 0
    mins = float('inf')
    
    for i in range(n):
        mins = min(mins, a[i])
        if mins < a[i]:
            total += mins
        else:
            total += a[i]
    
    print(total)