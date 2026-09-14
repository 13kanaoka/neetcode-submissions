class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            premap[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if premap[course] == []:
                return True

            visited.add(course)
            for prereq in premap[course]:
                if not dfs(prereq):
                    return False
            premap[course] = []
            visited.remove(course)
            return True

        for course in premap:
            if not dfs(course):
                return False

        return True