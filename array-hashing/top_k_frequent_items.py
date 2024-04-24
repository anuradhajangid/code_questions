from collections import Counter
from heapq import *

class Solution(object):
    def topKFrequent_approach1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = {}
        for number in nums:
            try:
                freq_dict[number] += 1
            except KeyError:
                freq_dict[number] = 1
        key_value_tuples = [(value, key) for key, value in freq_dict.items()]
        key_value_tuples.sort(key=lambda x:x[0], reverse=True)
        return_list = []
        for i in range(k):
            return_list.append(key_value_tuples[i][1])
        return return_list
    
    def topKFrequent_approach2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums
        freq_dict = Counter(nums)
        heap = []
        for key in freq_dict:
            heappush(heap, (-freq_dict[key], key))
        result = []
        while k > 0:
            result.append(heappop(heap)[1])
            k -= 1
        return result
    
assert Solution().topKFrequent_approach1(nums = [1,1,1,2,2,3], k = 2) == [1,2]
assert Solution().topKFrequent_approach1(nums = [1], k = 1) == [1]

assert Solution().topKFrequent_approach2(nums = [1,1,1,2,2,3], k = 2) == [1,2]
assert Solution().topKFrequent_approach2(nums = [1], k = 1) == [1]
