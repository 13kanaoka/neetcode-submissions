class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = { i:[] for i in range(n) }
        for node_a, node_b in edges:
            adj[node_a].append(node_b)
            adj[node_b].append(node_a)
        
        visited = set()
        def dfs(curr, parent):
            if curr in visited:
                return False

            visited.add(curr)
            for neighbor in adj[curr]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, curr):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n