class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            premap[course].append(prereq)
        
        path = set()
        def dfs(course):
            if premap[course] == []:
                return True
            if course in path:
                return False
            
            path.add(course)
            for prereq in premap[course]:
                if not dfs(prereq):
                    return False
                
            premap[course] = []
            path.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True