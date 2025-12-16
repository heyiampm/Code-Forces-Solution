#Problem name:("Normal Problem")//(Code forces problem 04)

t = int(input())
for _ in range(t):
          a = input().strip()
          mirror = {'p':'q', 'q':'p', 'w':'w'}
          b = '' 
          for ch in reversed(a):
                    b += mirror[ch]
                    print(b)
