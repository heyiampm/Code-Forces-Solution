#Problem name:("A+B Again?")//(Code forces problem 07)

t = int(input())
for i in range(t):
          n = int(input())
          first  = n // 10
          sec  = n % 10
          sum_digit = first + sec
          print(sum_digit)