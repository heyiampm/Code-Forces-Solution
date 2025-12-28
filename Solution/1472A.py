#Problem name:("Cards for Friends")//(Code forces problem 47)

for _ in range(int(input())):
    w,h,n=map(int,input().split())
    c=1
    while w%2==0: w//=2; c*=2
    while h%2==0: h//=2; c*=2
    print("YES" if c>=n else "NO")