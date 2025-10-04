
from typing import List
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Create graph
        indegree = [0] * numCourses
        adj = [[] for _ in prerequisites]

        for a,b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
        
        task = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                task.append(i)
        order = []

        while task:
            course = task.popleft()
            order.append(course)
            for v in adj[course]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    task.append(v)
        if len(order) == numCourses:
            return order
        return []
    

"""
numCourse = 4
prereq: [[1,0], [2,0], [3, 1], [3,2]]
indegree = [0,1,1,2]
adj = [[1,2],[3],[3],[]]

task = 3
order=[0,1,2,3]
course = 3
v = []
indegree = [0,0,0,0]

numCourse = 4
prereq: [[1,0], [2,1], [3, 2], [0,3]]
indegree = [1,1,1,1]
adj = [[1,2],[3],[3],[]]

task = 3
order=[0,1,2,3]
course = 3
v = []
indegree = [0,0,0,0]

numCourse = 4
prereq: [[2,1], [3, 2], [3,1]]
indegree = [0,0,1,2]
adj = [[],[2,3],[3],[]]

task = 3
order=[0,1,2,3]
course = 3
v = []
indegree = [0,0,0,0]

"""

        
