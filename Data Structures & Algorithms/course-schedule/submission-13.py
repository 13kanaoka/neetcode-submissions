class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        path = set()
        def dfs(course):
            if course in path:
                return False
            if premap[course] == []:
                return True
            
            path.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            premap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True