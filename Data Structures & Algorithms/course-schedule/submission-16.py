class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visit = set()
        def dfs(course):
            if premap[course] == []:
                return True
            if course in visit:
                return False
            
            visit.add(course)
            for prereq in premap[course]:
                if not dfs(prereq):
                    return False
            premap[course] = []
            visit.remove(course)
            return True
        
        for course in premap:
            if not dfs(course):
                return False
        return True