# Problem can be found at https://codeforces.com/problemset/problem/1791/A

t = int(input())
for _ in range(t):
          char = input().lower()
          word = "codeforces"
          if char in word and len(char)==1:
                    print("YES")
          elif len(char):
                    print("NO")
          else:
                    print("YES")