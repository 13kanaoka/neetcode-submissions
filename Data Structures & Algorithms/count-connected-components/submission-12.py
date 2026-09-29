class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        sizes = [1] * n

        def find(node):
            root = node

            while root != par[root]:
                par[root] = par[par[root]]
                root = par[root]
            
            return root
        
        def union(a, b):
            rootA, rootB = find(a), find(b)

            if rootA == rootB:
                return 0
            
            if sizes[rootA] < sizes[rootB]:
                rootA, rootB = rootB, rootA
            
            par[rootB] = par[rootA]
            sizes[rootA] += sizes[rootB]
            return 1
        
        count = n
        for a, b in edges:
            count -= union(a, b)
        return count