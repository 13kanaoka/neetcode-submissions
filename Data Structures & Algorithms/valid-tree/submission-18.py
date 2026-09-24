class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = { i:[] for i in range(n) }
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()
        def dfs(curr, prev):
            if curr in visit:
                return False
            
            visit.add(curr)
            for child in adj[curr]:
                if child == prev:
                    continue
                if not dfs(child, curr):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)