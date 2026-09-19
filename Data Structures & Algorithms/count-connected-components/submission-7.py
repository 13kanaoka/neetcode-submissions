class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n

        def find(node):
            root = node

            while root != parent[root]:
                parent[root] = parent[parent[root]]
                root = parent[root]
            return root

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