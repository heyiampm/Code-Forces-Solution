import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    Y = int(input_data[0])
    W = int(input_data[1])
    
    max_val = max(Y, W)
    numerator = 6 - max_val + 1
    denominator = 6
    
    common_divisor = math.gcd(numerator, denominator)
    
    print(f"{numerator // common_divisor}/{denominator // common_divisor}")

if __name__ == '__main__':
    solve()