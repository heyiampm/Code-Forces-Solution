# Problem can be found at https://codeforces.com/problemset/problem/546/A

k,n,w = list(map(int, input().split()))
cost = k*w*(w+1)//2
print(max(0,cost-n))