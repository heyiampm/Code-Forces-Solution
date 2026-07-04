import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    out = []
    
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        a = [int(x) for x in input_data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        possible = True
        next_min = float('inf')
        
        # Traverse backward
        for i in range(n - 1, -1, -1):
            if a[i] <= next_min:
                # Keep it as a whole number
                next_min = a[i]
            else:
                # Must split it into digits
                tens = a[i] // 10
                ones = a[i] % 10
                
                if tens <= ones <= next_min:
                    next_min = tens
                else:
                    possible = False
                    break
                    
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()