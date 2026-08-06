import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    
    pi = [0] * n
    max_mid = 0

    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

        if i < n - 1:
            max_mid = max(max_mid, pi[i])

    res = pi[n - 1]

    while res > max_mid:
        res = pi[res - 1]

    if res <= 0:
        print("Just a legend")
    else:
        print(s[:res])


if __name__ == "__main__":
    main()