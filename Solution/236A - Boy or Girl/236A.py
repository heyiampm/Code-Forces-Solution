# Problem can be found at https://codeforces.com/problemset/problem/236/A

s = input().strip()
dis_count = len(set(s))
if dis_count % 2== 0:
          print("CHAT WITH HER!")
else:
          print("IGNORE HIM!") 