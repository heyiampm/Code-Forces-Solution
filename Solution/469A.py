#Problem name:("I Wanna Be the Guy")//(Code forces problem 39)

n = int(input())
levels = set()
for _ in range(2):
    a = list(map(int, input().split()))
    levels |= set(a[1:])
print("I become the guy." if len(levels) == n else "Oh, my keyboard!")
