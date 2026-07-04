import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    groups = [int(x) for x in input_data[1:]]
    
    counts = Counter(groups)
    
    taxis = counts[4]
    
    taxis += counts[3]
    counts[1] = max(0, counts[1] - counts[3])
    
    taxis += counts[2] // 2
    if counts[2] % 2 != 0:
        taxis += 1
        counts[1] = max(0, counts[1] - 2)
        
    if counts[1] > 0:
        taxis += (counts[1] + 3) // 4
        
    print(taxis)

if __name__ == '__main__':
    solve()