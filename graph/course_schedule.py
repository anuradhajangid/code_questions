#https://leetcode.com/problems/course-schedule/
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = [[] for _ in range(numCourses)]
        visited = [None for _ in range(numCourses)]
        for course,required in prerequisites:
            adj_list[course].append(required)
        def dfs(course):
            if visited[course] != None:
                return visited[course]
            visited[course] = False
            for required in adj_list[course]:
                if not dfs(required):
                    return False
            visited[course] = True
            return True
        for co in range(numCourses):
            if not dfs(co):
                return False
        return True

numCourses = 2
prerequisites = [[1,0]]
assert Solution().canFinish(numCourses,prerequisites) == True
prerequisites = [[1,0],[0,1]]
assert Solution().canFinish(numCourses,prerequisites) == False
numCourses = 1
prerequisites = []
assert Solution().canFinish(numCourses,prerequisites) == True

