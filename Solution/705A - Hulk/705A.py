# Problem can be found at https://codeforces.com/problemset/problem/705/A

def hulk():
          n = int(input())
          ans = []
          for i in range(1, n+1):
                    if i % 2 == 1:
                              ans.append("I hate")
                    else:
                              ans.append("I love")
          final = " that ".join(ans)
          final += " it"
          print(final)
hulk()