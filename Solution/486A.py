#Problem name:("Calculating Function")//(Code forces problem 61)

n = int(input())
if n % 2 == 0:
          f = n / 2
else:
          f = (-1)*(n/2+1)
print(int(f))