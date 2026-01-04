#Problem name:("Triangle")//(Day 41)

a=sorted(map(int,input().split()))
ok=seg=0
for i in range(4):
    x=[a[j] for j in range(4) if j!=i]
    if x[0]+x[1]>x[2]: ok=1
    elif x[0]+x[1]==x[2]: seg = 1
print("TRIANGLE" if ok else "SEGMENT" if seg else "IMPOSSIBLE")
