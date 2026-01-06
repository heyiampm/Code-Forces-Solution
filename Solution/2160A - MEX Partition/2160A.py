# Problem can be found at https://codeforces.com/problemset/problem/2160/A

t = int(input())
for _ in range(t):
          n = int(input())
          A = list(map(int, input().split()))
          mex = 0
          while mex in A:
                    mex+=1
          print(mex) 