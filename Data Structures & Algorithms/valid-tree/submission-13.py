class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = { i:[] for i in range(n) }
        for nodeA, nodeB in edges:
            adj[nodeA].append(nodeB)
            adj[nodeB].append(nodeA)
        
        visited = set()
        def dfs(currNode, prevNode):
            if currNode in visited:
                return False

            visited.add(currNode)
            for neighbor in adj[currNode]:
                if neighbor == prevNode:
                    continue
                if not dfs(neighbor, currNode):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n