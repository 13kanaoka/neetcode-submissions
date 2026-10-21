class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i:[] for i in range(numCourses) }
        for pre, crs in prerequisites:
            premap[crs].append(pre)
        
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            
            if premap[course] == []:
                return True
            
            visit.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
                
            premap[course] = []
            visit.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
