# Problem can be found at https://codeforces.com/problemset/problem/271/A

year = int(input())
while True:
          year += 1
          s = str(year)
          if len(set(s)) == len(s):
                    print(year)
                    break 