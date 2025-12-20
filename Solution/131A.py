#Problem name:("cAPS lOCK")//(Code forces problem 25)

t = input()
if t.isupper() or (len(t)==1) or t[1:].isupper():
          print(t.swapcase())
else:
          print(t)