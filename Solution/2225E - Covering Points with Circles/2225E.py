import sys
import math

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    r = int(input_data[1])
    
    points = []
    idx = 2
    for _ in range(n):
        px = int(input_data[idx])
        py = int(input_data[idx+1])
        points.append((px, py))
        idx += 2
        
    
    H = math.ceil(math.sqrt(3) * r)
    
    chosen_centers = set()
    
    for px, py in points:
        
        approx_j = py // H
        
        found = False
        
        for j in range(approx_j - 2, approx_j + 3):
            Y = j * H
            shift = (j % 2) * r
            
           
            approx_i = (px - shift) // (2 * r)
            
            for i in range(approx_i - 2, approx_i + 3):
                X = 2 * i * r + shift
                
                
                if (px - X) ** 2 + (py - Y) ** 2 <= r * r:
                    chosen_centers.add((X, Y))
                    found = True
                    break
            if found:
                break

   
    print(len(chosen_centers))
    for cx, cy in chosen_centers:
        print(f"{cx} {cy}")

if __name__ == '__main__':
    solve()