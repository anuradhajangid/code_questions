from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        N = len(arr)
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[N-k:]
        for end in range(len(arr)):
            if end - start + 1 == k:
                if end != N-1 and abs(x-arr[end+1]) >= abs(x-arr[start]) and arr[end+1] != arr[end]:
                    break
                start += 1
        return arr[start:end+1]
    
assert Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3) == [1,2,3,4]
assert Solution().findClosestElements(arr = [1,1,2,3,4,5], k = 4, x = -1) == [1,1,2,3]
assert Solution().findClosestElements(arr = [1,1,2,3,4,5], k = 4, x = 6) == [2,3,4,5]
assert Solution().findClosestElements(arr = [1,1,1,10,10,10], k = 1, x = 9) == [10]
å