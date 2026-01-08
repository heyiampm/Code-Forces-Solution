# Problem can be found at https://codeforces.com/problemset/problem/339/A

s = input()
nums = s.split('+')
nums.sort()
print('+'.join(nums))