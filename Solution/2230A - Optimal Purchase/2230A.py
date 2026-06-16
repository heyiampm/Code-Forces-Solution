import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    index = 1
    for _ in range(t):
        n = int(data[index])
        a = int(data[index+1])
        b = int(data[index+2])
        index += 3
        if 3 * a <= b:
            cost = n * a
        else:
            full_groups = n // 3
            rem = n % 3
            
            if rem == 0:
                cost = full_groups * b
            else:
                cost = full_groups * b + min(rem * a, b)
                
        results.append(str(cost))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()