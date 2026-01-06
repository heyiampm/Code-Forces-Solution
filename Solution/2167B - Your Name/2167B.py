# Problem can be found at https://codeforces.com/problemset/problem/2167/B

q = int (input())
for _ in range(q):
          n = int(input())
          s , t = input().split()
          if sorted(s) == sorted(t):
                    print("YES")
          else:
                    print("NO")