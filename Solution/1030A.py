#Problem name:("In Search of an Easy Problem")//(Code forces problem 58)

n = int(input())
a = list(map(int, input().split()))
if sum(a): 
          print('HARD')
else:
          print('EASY')
