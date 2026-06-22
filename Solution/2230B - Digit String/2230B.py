import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        s = data[i]
        
        deletions = 0
        filtered = []
        for c in s:
            if c == '4':
                deletions += 1
            else:
                filtered.append(c)
        
        total_2 = 0
        for c in filtered:
            if c == '2':
                total_2 += 1
                
        min_removals = total_2
        current_2 = 0
        current_13 = 0
        
        for c in filtered:
            if c == '2':
                current_2 += 1
            else:
                current_13 += 1
                
            removals_if_split_here = current_13 + (total_2 - current_2)
            if removals_if_split_here < min_removals:
                min_removals = removals_if_split_here
                
        results.append(str(deletions + min_removals))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()