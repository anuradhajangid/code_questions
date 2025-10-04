class Solution():
    def cuttingRibbon(self, ribbons, k):
        right = max(ribbons)
        left = 1
        while left <= right:
            mid = left + (right-left)//2
            if Solution.can_cut(ribbons, k, mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    @staticmethod
    def can_cut(ribbons, k, mid):
        count = 0
        for ribbon in ribbons:
            count = ribbons//mid
            if count >= k:
                return True
        return False