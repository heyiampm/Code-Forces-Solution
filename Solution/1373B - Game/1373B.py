#Problem can be found at  https://codeforces.com/problemset/problem/1373/B

t_str = input()
if t_str:
          t = int(t_str)
          for _ in range(t):
                    s = input()
                    count_0 = s.count('0')
                    count_1 = s.count('1')
                    total_moves = min(count_0, count_1)
                    if total_moves % 2 == 1:
                              print("DA")
                    else:
                              print("NET")
