#Problem name:("Boy or Girl")//(Code forces problem 56)

s = input().strip()
dis_count = len(set(s))
if dis_count % 2== 0:
          print("CHAT WITH HER!")
else:
          print("IGNORE HIM!")