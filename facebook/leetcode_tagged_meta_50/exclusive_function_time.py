from collections import deque
from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        call_stack = deque()
        function_time = [0] * n
        helper = lambda log: (int(log[0]), log[1], int(log[2]))
        for log in logs:
            id,state,time  = helper(log.split(":"))
            if state == "end":
                pr_id, pr_state, pr_time, pr_sum = call_stack.pop()
                function_time[id] += time - pr_time + 1 + pr_sum
                if call_stack:
                    call_stack[-1][2] = time+1
            else:
                if call_stack:
                    function_time[call_stack[-1][0]] +=  time - call_stack[-1][2]
                call_stack.append([id,state,time,0])
        return function_time
    
assert Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]) == [3,4]
    
"""
Examples
2, ["0:start:0","1:start:2","1:end:5","0:end:6"]
Callstack = [(0,start,6,2) ]
function_time=[3,4]

1, 
["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
Callstack = [(0,start,7,2) ]
function_time [8]

n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
Callstack = [(0,start,7,2)]
function_time = [7, 1]

n=1, ["0:start:0","0:start:1","0:start:2","0:end:3","0:end:4","0:end:5"]
Callstack = [[0,start,5,4]]
function_time = [8]
"""
