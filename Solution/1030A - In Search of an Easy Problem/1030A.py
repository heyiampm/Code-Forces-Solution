# Problem can be found at https://codeforces.com/problemset/problem/1030/A

n = int(input())
a = list(map(int, input().split()))
if sum(a): 
          print('HARD')
else:
          print('EASY')