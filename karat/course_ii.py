#https://leetcode.com/problems/course-schedule-ii/description/
from typing import List
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        order = []
        queue = deque()
        for index, degree in enumerate(indegree):
            if degree == 0:
                queue.append(index)
        
        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbour in adj[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return order if len(order) == numCourses else []
    
assert Solution().findOrder(numCourses = 2, prerequisites = [[1,0]]) == [0,1]
assert Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]) == [0,2,1,3]