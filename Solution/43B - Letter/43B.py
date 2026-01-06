# Problem can be found at https://codeforces.com/problemset/problem/43/B

from collections import Counter
s1 = input()
s2 = input()
c1 = Counter(s1.replace(' ',''))
c2 = Counter(s2.replace(' ',''))
print("YES" if c2 <= c1 else "NO")