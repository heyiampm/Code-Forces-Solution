#Problem name:("Codeforces Checking")//(Code forces problem 22)

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