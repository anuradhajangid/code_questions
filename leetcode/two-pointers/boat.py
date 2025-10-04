from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r,count=0,len(people)-1,0

        while l<=r:
            if people[l] + people[r] <= limit:
                l += 1
                count += 1
            else:
                count +=1
            r -= 1
            
        return count

assert Solution().numRescueBoats(people = [1,2], limit = 3) == 1
assert Solution().numRescueBoats(people = [3,2,2,1], limit = 3) == 3
assert Solution().numRescueBoats(people = [3,5,3,4], limit = 5) == 4