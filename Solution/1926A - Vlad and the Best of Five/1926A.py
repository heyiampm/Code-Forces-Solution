# Problem can be found at https://codeforces.com/problemset/problem/1926/A

t = int(input())
for _ in range(t):
          s = input()
          a = s.count('A')
          b = s.count('B')
          if a > b:
                    print('A')
          else:
                    print('B')