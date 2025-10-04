#https://leetcode.com/problems/naming-a-company/description/
from collections import defaultdict
from typing import List
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        nameMap =  defaultdict(set)
        for idea in ideas:
            nameMap[idea[0]].add(idea[1:])
        result = 0
        for name1 in nameMap:
            for name2 in nameMap:
                if name1 == name2:
                    continue

                common = 0
                for value in nameMap[name1]:
                    if value in nameMap[name2]:
                        common += 1

                result += (len(nameMap[name1])-common) * (len(nameMap[name2]) - common)
        return result
         

        

assert Solution().distinctNames(ideas = ["coffee","donuts","time","toffee"]) == 6
assert Solution().distinctNames(ideas = ["lack","back"]) == 0
