# Problem can be found at https://codeforces.com/problemset/problem/1999/A

t = int(input())
for i in range(t):
          n = int(input())
          first  = n // 10
          sec  = n % 10
          sum_digit = first + sec
          print(sum_digit)