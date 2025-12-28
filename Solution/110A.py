#Problem name:("Nearly Lucky Number")//(Code forces problem 46)

n = input()
count = 0
for digit in n:
    if digit == '4' or digit == '7':
        count += 1
        if count == 4 or count == 7:
            print("YES")
        else:
            print("NO")
