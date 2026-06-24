import sys
from bisect import bisect_left, bisect_right

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    names = [0] * (n + 1)
    name_to_id = {}
    id_counter = 0
    
    adj = [[] for _ in range(n + 1)]
    roots = []
    
    idx = 1
    for i in range(1, n + 1):
        name_str = input_data[idx]
        p = int(input_data[idx+1])
        idx += 2
        
        if name_str not in name_to_id:
            name_to_id[name_str] = id_counter
            id_counter += 1
        names[i] = name_to_id[name_str]
        
        if p == 0:
            roots.append(i)
        else:
            adj[p].append(i)
            
    m = int(input_data[idx])
    idx += 1
    
    queries_by_depth = {}
    for q_idx in range(m):
        v = int(input_data[idx])
        k = int(input_data[idx+1])
        idx += 2
        queries_by_depth.setdefault(v, []).append((k, q_idx))
        
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    depth = [0] * (n + 1)
    timer = 0
    
    nodes_by_depth = {}
    
    for root in roots:
        stack = [(root, 0, 0)]
        while stack:
            u, d, state = stack.pop()
            if state == 0:
                timer += 1
                tin[u] = timer
                depth[u] = d
                nodes_by_depth.setdefault(d, []).append(u)
                stack.append((u, d, 1))
                for v in reversed(adj[u]):
                    stack.append((v, d + 1, 0))
            else:
                tout[u] = timer

    queries_at_depth = {}
    for v, q_list in queries_by_depth.items():
        d_v = depth[v]
        t_in = tin[v]
        t_out = tout[v]
        for k, q_idx in q_list:
            target_d = d_v + k
            queries_at_depth.setdefault(target_d, []).append((t_in, t_out, q_idx))
            
    ans = [0] * m
    last_pos = [-1] * id_counter
    
    for d, nodes in nodes_by_depth.items():
        if d not in queries_at_depth:
            continue
            
        tins = [tin[u] for u in nodes]
        v_names = [names[u] for u in nodes]
        sz = len(nodes)
        
        bit = [0] * (sz + 1)
        
        def update(i, delta):
            while i <= sz:
                bit[i] += delta
                i += i & (-i)
                
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        d_queries = queries_at_depth[d]
        mapped_queries = []
        for t_in, t_out, q_idx in d_queries:
            l = bisect_left(tins, t_in)
            r = bisect_right(tins, t_out) - 1
            if l <= r:
                mapped_queries.append((l, r, q_idx))
                
        mapped_queries.sort(key=lambda x: x[1])
        
        q_ptr = 0
        num_queries = len(mapped_queries)
        
        for r in range(sz):
            name_id = v_names[r]
            if last_pos[name_id] != -1:
                update(last_pos[name_id] + 1, -1)
            last_pos[name_id] = r
            update(r + 1, 1)
            
            while q_ptr < num_queries and mapped_queries[q_ptr][1] == r:
                ql, qr, q_idx = mapped_queries[q_ptr]
                ans[q_idx] = query(qr + 1) - query(ql)
                q_ptr += 1
                
        for u in nodes:
            last_pos[names[u]] = -1

    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    solve()