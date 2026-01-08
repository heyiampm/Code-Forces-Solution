# Problem can be found at https://codeforces.com/problemset/problem/118/B

n = int(input())
for i in list(range(n + 1)) + list(range(n - 1, -1, -1)):
    print("  " * (n - i) + " ".join(map(str, list(range(i + 1)) + list(range(i - 1, -1, -1)))))