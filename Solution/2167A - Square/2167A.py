# Problem can be found at https://codeforces.com/problemset/problem/2167/A

t = int(input())
for _ in range(t):
          sticks = list(map(int, input().split()))
          if sticks.count(sticks[0]) == 4:
                    print("Yes")
          else:
                    print("NO")