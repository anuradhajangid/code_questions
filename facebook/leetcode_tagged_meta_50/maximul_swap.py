#https://leetcode.com/problems/maximum-swap/description/?envType=problem-list-v2&envId=7p59281

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        max_c=-1
        max_v= "0"
        swap_i = swap_j = -1
        for i in reversed(range(len(num_str))):
            if num_str[i] > max_v:
                max_v = num_str[i]
                max_c = i
            if num_str[i] < max_v:
                swap_i = i
                swap_j = max_c
        num_str[swap_j], num_str[swap_i] = num_str[swap_i], num_str[swap_j]

        return int("".join(num_str))
    
assert Solution().maximumSwap(num =99901) == 99910
assert Solution().maximumSwap(num = 120) == 210
assert Solution().maximumSwap(num = 2736) == 7236
assert Solution().maximumSwap(num = 9973) == 9973
