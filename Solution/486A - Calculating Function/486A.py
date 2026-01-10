# Problem can be found at https://codeforces.com/problemset/problem/486/A

n = int(input())
if n % 2 == 0:
          f = n / 2
else:
          f = (-1)*(n/2+1)
print(int(f))