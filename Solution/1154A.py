#Problem name:("Restoring Three Numbers")//(Code forces problem 48)

nums = list(map(int, input().split()))
nums.sort()
p, q, r, S = nums
a = S - r
b = S - q
c = S - p
print(a, b, c)