#Problem name:("Anton and Danik")//(Code forces problem 55)

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