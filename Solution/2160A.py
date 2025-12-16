#Problem name:("MEX Partition")//(Code forces problem 14)
t = int(input())
for _ in range(t):
          n = int(input())
          A = list(map(int, input().split()))
          mex = 0
          while mex in A:
                    mex+=1
          print(mex)