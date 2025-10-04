
from collections import defaultdict
class Solution():
    def __init__(self, nums):
        self.map = defaultdict()
        for i, num in enumerate(nums):
            self.map[i] = num
    
    def dotProduct(self, other):
        product = 0
        for key, value in self.map.items():
            if key in other.map:
                product += value * other.map[key]
        return product

# do not use map and O(N) complexity
class Solution():
    def __init__(self, nums):
        self.map = []
        for i, num in enumerate(nums):
            self.map.append([i,num])
    
    def dotProduct(self, other):
        product = 0
        i = 0
        j = 0
        while i < len(self.map) and j < len(other.map):
            if self.map[i][0] == other.map[j][0]:
                product += self.map[i][0] * other.map[j][0]
                i += 1
                j += 1
            elif self.map[i][0] < other.map[j][0]:
                i += 1
            else:
                j += 1
            
        return product

# Optimized for logN
class Solution():
    def __init__(self, nums):
        self.map = []
        for i, num in enumerate(nums):
            self.map.append([i,num])
    
    def dotProduct(self, other):
        product = 0
        start = 0
        end = len()
        for index, num in enumerate(self.map):
            data = Solution.binary_search(other, index)
            if data:
                product += num * data[1]
        return product
    
    @staticmethod
    def binary_search(vector, index):
        start = 0
        end = len(vector) -1
        while start < end:
            mid = start + (end - start)//2
            if vector[mid][0] == index:
                return vector[mid]
            elif vector[mid][0] > index:
                end = mid -1
            else:
                start = mid + 1
        return None
