class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        path = set()
        def dfs(course):
            if course in path:
                return False
            if adj[course] == []:
                return True

            path.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            adj[course] = []
            return True
        
        for course in adj:
            if not dfs(course):
                return False
        return True