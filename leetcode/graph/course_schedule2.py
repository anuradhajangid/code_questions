#https://leetcode.com/problems/course-schedule/
from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = defaultdict(list)
        for x,y in prerequisites:
            if x not in adj_list:
                adj_list[x] = []
            adj_list[x].append(y)
        visited = {}
        reveresePO = []
        def dfs(course):
            if course in visited:
                return visited[course]
            visited[course] = True
            for required in adj_list[course]:
                if dfs(required):
                    return True
            visited[course] = False
            reveresePO.append(course)
            
        for co in range(numCourses):
            if dfs(co):
                return []

        return reveresePO

numCourses = 2
prerequisites = [[1,0]]
assert Solution().canFinish(numCourses,prerequisites) == [0,1]
numCourses = 2
prerequisites = [[1,0], [0,1]]
assert Solution().canFinish(numCourses,prerequisites) == []
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
assert Solution().canFinish(numCourses,prerequisites) == [0,1,2,3]
numCourses = 1
prerequisites = []
assert Solution().canFinish(numCourses,prerequisites) == [0]

