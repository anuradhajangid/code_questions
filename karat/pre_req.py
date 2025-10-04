#https://leetcode.com/problems/course-schedule/description/
from typing import List
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(set)
        for x,y in prerequisites:
            adj[y].add(x)
            indegree[x] += 1

        queue = deque()
        visited = set()
        for i in range(0,numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            visited.add(course)
            for neighbour in adj[course]:
                indegree[neighbour] -=1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return len(visited) == numCourses

assert Solution().canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]) == False
assert Solution().canFinish(numCourses = 2, prerequisites = [[1,0]]) == True