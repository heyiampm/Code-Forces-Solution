#Problem name:("Clock Conversion")//(Code forces problem 12

for _ in range(int(input())):
          hh, mm = map(int, input().split(":"))
          time = "AM" if hh < 12 else "PM"
          hh = hh % 12 or 12
          print(f"{hh:02d}:{mm:02d} {time}")