class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = { i:[] for i in range(n) }
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            for neighbor in adj[curr]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, curr):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n