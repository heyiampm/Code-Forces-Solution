#Problem name:("Soldier and Bananas")//(Code forces problem 51)

k,n,w = list(map(int, input().split()))
cost = k*w*(w+1)//2
print(max(0,cost-n))
