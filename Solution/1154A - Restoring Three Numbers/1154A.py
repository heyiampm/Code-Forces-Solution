# Problem can be found at https://codeforces.com/problemset/problem/1154/A

nums = list(map(int, input().split()))
nums.sort()
p, q, r, S = nums
a = S - r
b = S - q
c = S - p
print(a, b, c)