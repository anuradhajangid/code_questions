from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for ana in strs:
            sortedana = sorted(ana)
            if sortedana in groups.keys():
                groups[sortedana].append(ana)
            else:
                groups[sortedana] = [ana]
        return list(groups.values())

assert (Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])) == sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
assert Solution().groupAnagrams([""]) == [[""]]
assert Solution().groupAnagrams(["a"]) == [["a"]]