#Problem name:("Way Too Long Words")//(Code forces problem 71)

for i in range(int(input())):
          s = input()
          if len(s) > 10:
                    print(s[0]+str(len(s)-2)+s[-1])
          else:
                    print(s)
