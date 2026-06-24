import sys

def count_rem(left, right, rem):
    if left > right:
        return 0
    
    def count_up_to(k, r):
        if k < 0:
            return 0
        ans = (k // 4)
        if (k % 4) >= r:
            ans += 1
        return ans

    return count_up_to(right, rem) - count_up_to(left - 1, rem)

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    MOD = 998244353
    
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx+1])
        idx += 2
        
        # Elements for r: x <= r <= n
        r_mod1 = count_rem(x, n, 1)
        r_mod3 = count_rem(x, n, 3)

        L_mod1 = count_rem(0, x - 1, 1)
        L_mod3 = count_rem(0, x - 1, 3)
        L_zero = 1 if x - 1 >= 0 else 0 
        
        # Total pairs
        ans = (r_mod1 * L_mod1) % MOD
        ans = (ans + r_mod3 * (L_mod3 + L_zero)) % MOD
        
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()