from typing import List
class Solution:
    def knapsackDynamic(self, weights, prices, capacity):
        """
        Time Complexity = O(C*n), where n = length of weights
        Space complexity = O(C*n), for storing the intermediate states 
        """
        memo = {}
        def _helper(weights, prices, capacity, index):
            if capacity <=0 or index >= len(weights):
                return 0
            if (capacity, index) in memo:
                return memo[(capacity, index)]
            if weights[index] > capacity:
                memo[(capacity,index)] = _helper(weights, prices, capacity, index + 1)
                return memo[(capacity, index)]
            memo[(capacity, index)] = max(prices[index] + _helper(weights, prices, capacity - weights[index], index + 1), _helper(weights, prices, capacity, index + 1))
            return memo[(capacity, index)]
        return _helper(weights, prices, capacity, 0)
    def knapsackBruteForce(self, weights, prices, capacity):
        """
        Time Complexity = O(2**n)
        Space complexity = constant
        """
        def _helper(weights, prices, capacity, index):
            if capacity <=0 or index >= len(weights):
                return 0
            if weights[index] > capacity:
                return _helper(weights, prices, capacity, index + 1)
            return max(prices[index] + _helper(weights, prices, capacity - weights[index], index + 1), _helper(weights, prices, capacity, index + 1))
        return _helper(weights, prices, capacity, 0)
assert Solution().knapsackDynamic([2,1,1,3], [2,8,1,10], 4) == 18