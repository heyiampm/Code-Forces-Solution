# Problem can be found at https://codeforces.com/problemset/problem/2044/B

t = int(input())
for _ in range(t):
          a = input().strip()
          mirror = {'p':'q', 'q':'p', 'w':'w'}
          b = '' 
          for ch in reversed(a):
                    b += mirror[ch]
                    print( b )