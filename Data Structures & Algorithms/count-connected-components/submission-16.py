class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [ i for i in range(n) ]
        sizes = [ 1 for _ in range(n) ]

        def find(node):
            root = node

            while root != par[root]:
                par[root] = par[par[root]]
                root = par[root]
            
            par[root] = root
            return root
        
        def union(a, b):
            rootA, rootB = find(a), find(b)

            if rootA == rootB:
                return 0
            
            if sizes[rootB] > sizes[rootA]:
                rootA, rootB = rootB, rootA
            
            par[rootB] = rootA
            sizes[rootA] += sizes[rootB]
            return 1
        
        count = n
        for a, b in edges:
            count -= union(a, b)
        return count