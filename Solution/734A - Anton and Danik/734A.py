# Problem can be found at https://codeforces.com/problemset/problem/734/A

n = int (input().strip())
t = input().strip()
anton = t.count('A')
danik = t.count('D')

if anton > danik:
          print("Anton")
elif  danik > anton:
          print("Danik")
else:
          print("Friendship") 