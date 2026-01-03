#Problem name:("Max Plus Size")//(Code forces problem 06)

for _ in range(int(input())):
          n = int(input())
          a = list(map(int, input().split()))
          odd_max = max(a[::2]) if n >= 1  else 0
          even_max = max(a[1::2]) if n > 1 else 0
          print(max(odd_max + (n+1)//2, even_max + n//2))