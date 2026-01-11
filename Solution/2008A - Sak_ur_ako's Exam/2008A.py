# Problem can be found at https://codeforces.com/problemset/problem/2008/A

t = int(input())
for _ in range(t):
          a, b = map(int, input().split())
          if (a + 2*b) % 2 == 0 and (b % 2 == 0 or a >= 2):
                    print("YES")
          else:
                    print("NO")