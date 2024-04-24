from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for ana in strs:
            strhash = hash(str(sorted(ana)))
            if strhash in groups.keys():
                groups[strhash].append(ana)
            else:
                groups[strhash] = [ana]
        return list(groups.values())

assert (Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])) == sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
assert Solution().groupAnagrams([""]) == [[""]]
assert Solution().groupAnagrams(["a"]) == [["a"]]