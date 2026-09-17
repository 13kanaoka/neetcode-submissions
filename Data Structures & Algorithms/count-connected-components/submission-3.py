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
            root_a, root_b = find(a), find(b)

            if root_a == root_b:
                return 0
            
            if size[root_b] > size[root_a]:
                root_a, root_b = root_b, root_a
            parent[root_a] = root_b
            size[root_b] += size[root_a]
            return 1
        
        count = n
        for a, b in edges:
            count -= union(a, b)
        return count