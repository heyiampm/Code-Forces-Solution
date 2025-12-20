#Problem name:("Beautiful Year")//(Code forces problem 24)

year = int(input())
while True:
          year += 1
          s = str(year)
          if len(set(s)) == len(s):
                    print(year)
                    break
