#https://leetcode.com/problems/expression-add-operators/description/?envType=problem-list-v2&envId=7p59281

from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        def backtrack(curr_index, current_res, current_sum, prev_num):
            nonlocal num
            if curr_index >= len(num):
                if current_sum == target:
                    result.append("".join(current_res))
                return
            for i in range(curr_index, len(num)):
                
                current_str = num[curr_index:i+1]
                current_num = int(current_str)
                if not current_res:
                    backtrack(i+1,[current_str], current_num, current_num)
                else:
                    backtrack(i+1, current_res + ['+'] +[current_str], current_sum + current_num, current_num)
                    backtrack(i+1, current_res + ['-'] +[current_str], current_sum - current_num, -current_num)
                    backtrack(i+1, current_res + ['*'] +[current_str], current_sum - prev_num + prev_num * current_num, current_num * prev_num)

                if num[curr_index] == '0':
                    break

        backtrack(0,[],0,0)
        return result
assert Solution().addOperators(num = "105", target = 5) == ["1*0+5","10-5"]
assert Solution().addOperators(num = "123", target = 6) == ["1+2+3","1*2*3"]
assert Solution().addOperators(num = "232", target = 8) == ["2+3*2","2*3+2"]
assert Solution().addOperators(num = "3456237490", target = 9191) == []
