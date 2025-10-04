from typing import List
#https://leetcode.com/problems/car-fleet/description/
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, reverse=True)
        fleet_stack = []

        for pos, sp in cars:
            time = (target-pos)/sp
            if fleet_stack and time <= fleet_stack[-1]:
                continue
            
            fleet_stack.append(time)
        
        return len(fleet_stack)
        


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

s = Solution()
s.carFleet(target, position, speed)