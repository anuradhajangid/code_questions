from typing import List

"""
Only need to warm the hoses not all indexes
"""
class Solution:
    def findRadius_min_radius_increase(self, houses: List[int], heaters: List[int]) -> int:
        uncovered_houses = set(houses) - set(heaters)
        ranges = [[heater, heater] for heater in heaters]
        radius =  0
        while uncovered_houses:
            radius += 1
            for rng in ranges:
                rng[0] -=1
                rng[1] += 1
                if rng[0] in uncovered_houses:
                    uncovered_houses.discard(rng[0])
                if rng[1] in uncovered_houses:
                    uncovered_houses.discard(rng[1])
        return radius
    

    def findRadius_min_dist_house_heater(self, houses: List[int], heaters: List[int]) -> int:
        dist = []
        for house in houses:
            distance = float("inf")
            for heater in heaters:
                if abs(house,heater) < distance:
                    distance = abs(house, heater)
            dist.append(distance)
        return max(dist)
    

    def findRadius_two_pointer(self, houses: List[int], heaters: List[int]) -> int:
        i = 0
        j = i+1
        dist = float("-inf")
        for house in houses:
            if heaters[i] < house < heaters[j]:
                dist = max(dist,min(abs(house, heaters[i]), abs(house, heaters[j])))
            elif house > heaters[j]:
                i += 1
                j +=1
                continue
            elif house < heaters[i]:
                dist = max(dist, abs(house-heaters[i]))
        return dist
                
