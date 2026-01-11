# Problem can be found at https://codeforces.com/problemset/problem/1948/A

import sys
def solve():
    input_data = sys.stdin.read().split()
    for n in map(int, input_data[1:]):
        if n % 2:
            print("NO")
        else:
            print("YES")
            print("".join(chr(65 + (i % 2)) * 2 for i in range(n // 2)))
solve()
