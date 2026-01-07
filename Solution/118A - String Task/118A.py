# Problem can be found at https://codeforces.com/problemset/problem/118/A

x = input()
str = ""
for i in x:
          if i.lower() not in "aeiouy":
                    str = str + "." + i.lower()
                    print(str)