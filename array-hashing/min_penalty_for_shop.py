#https://leetcode.com/problems/minimum-penalty-for-a-shop/
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        negmaxpenalty = 0
        negpenalty = 0
        hour = -1
        for hr, status in enumerate(customers):
            negpenalty += 1 if status == "Y" else -1
            if negpenalty > negmaxpenalty:
                negmaxpenalty = negpenalty
                hour = hr
        return hour + 1


assert Solution().bestClosingTime(customers = "YYNY") == 2
assert Solution().bestClosingTime(customers = "NNNNN") == 0
assert Solution().bestClosingTime(customers = "YYYY") == 4
