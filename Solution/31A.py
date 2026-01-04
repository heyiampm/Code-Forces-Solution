#Problem name:("Worms Evolution")//(Day 32)


n = int(input())
a = list(map(int, input().split()))
for i in range(n):
          for j in range(n):
                    for k in range(n):
                              if i != j and j != k and i != k:
                                        if a[i] == a[j] + a[k]:
                                                  print(i + 1, j + 1, k + 1)
                                                  exit ()
                    
print("-1")