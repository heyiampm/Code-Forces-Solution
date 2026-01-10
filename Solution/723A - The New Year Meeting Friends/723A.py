# Problem can be found at https://codeforces.com/problemset/problem/723/A

x , y ,z = map(int,input().split())
print(max(x,y,z) - min (x,y,z))