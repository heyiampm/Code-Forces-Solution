#Problem name:("String Task")//(Code forces problem 59)

x = input()
str = ""
for i in x:
          if i.lower() not in "aeiouy":
                    str = str + "." + i.lower()
                    print(str)