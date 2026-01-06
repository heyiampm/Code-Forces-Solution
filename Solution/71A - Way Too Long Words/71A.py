# Problem can be found at https://codeforces.com/problemset/problem/71/A

for i in range(int(input())):
          s = input()
          if len(s) > 10:
                    print(s[0]+str(len(s)-2)+s[-1])
          else:
                    print(s)
