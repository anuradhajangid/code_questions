from typing import List
class Solution:
    def knapsackDynamic_TD(self, weights, prices, capacity):
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
    def knapsackDynamic_BU(self, weights, prices, capacity):
        """
        Time Complexity = O(C*n), where n = length of weights
        Space complexity = O(C), for storing the intermediate states 
        """
        n = len(weights)
        table = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]
        def _helper(capacity, index):
            if capacity <=0 or index==0:
                return 0
            if table[index][capacity] != -1 :
                return table[index][capacity]
            if weights[index-1] <= capacity:
                table[index][capacity] = max(prices[index-1] + _helper(capacity-weights[index-1], index-1), _helper(capacity, n-1))
                return table[index][capacity]
            table[n][capacity] = _helper(capacity, weights, prices, index-1)
        
        return _helper(capacity, n)

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
assert Solution().knapsackDynamic_BU([2,1,1,3], [2,8,1,10], 4) == 18