class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = { i:[] for i in range(n) }
        for nodeA, nodeB in edges:
            adj[nodeA].append(nodeB)
            adj[nodeB].append(nodeA)
        
        visited = set()
        def dfs(currNode, parent):
            if currNode in visited:
                return False

            visited.add(currNode)
            for neighbor in adj[currNode]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, currNode):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n