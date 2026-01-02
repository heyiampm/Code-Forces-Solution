#Problem name:("Candies and Two Sisters")//(Code forces problem 63)

no = int(input())
for i in range(0, no):
          a = int(input())
          if a >= 0 and a <= 2:
                    print(0)
          else:
                    if a % 2 == 0:
                              t = (a/2)-1
                              print(int(t))
                    else:
                              t =int (a/2)
                              print(t)