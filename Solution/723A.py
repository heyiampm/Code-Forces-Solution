#Problem name:("The New Year: Meeting Friends")//(Code forces problem 23)

x , y ,z = map(int,input().split())
print(max(x,y,z) - min (x,y,z))