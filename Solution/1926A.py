#Problem name:("Vlad and the Best of Five")//(Code forces problem 40)

t = int(input())
for _ in range(t):
          s = input()
          a = s.count('A')
          b = s.count('B')
          if a > b:
                    print('A')
          else:
                    print('B')