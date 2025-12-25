#Problem name:("Present from Lena")//(Code forces problem 37)

n = int(input())
for i in list(range(n + 1)) + list(range(n - 1, -1, -1)):
    print("  " * (n - i) + " ".join(map(str, list(range(i + 1)) + list(range(i - 1, -1, -1)))))
