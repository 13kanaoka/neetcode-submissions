class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [ i for i in range(n) ]
        size = [1] * n

        def find(node):
            if parent[node] == node:
                return node
            
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            
            return node
        
        def union(a, b):
            rootA, rootB = find(a), find(b)

            if rootA == rootB:
                return 0
            
            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA
            parent[rootB] = rootA
            size[rootA] += size[rootB]
            return 1

        count = n
        for a, b in edges:
            count -= union(a, b)
        return count
