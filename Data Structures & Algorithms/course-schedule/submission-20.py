class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i:[] for i in range(numCourses) }
        for pre, crs in prerequisites:
            premap[crs].append(pre)

        visit = set()
        def dfs(course):
            if premap[course] == []:
                return True
            
            if course in visit:
                return False
            
            visit.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            premap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True