#https://leetcode.com/problems/remove-invalid-parentheses/editorial/?envType=problem-list-v2&envId=7p59281
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.result = set()
        self.max_len = -1
        self.dfs(s, 0, [], 0, 0)
        return list(self.result)

    def dfs(self, input, index, curr_res, left, right):
        if index >= len(input):
            if left == right:
                if len(curr_res) > self.max_len:
                    self.result = set()
                    self.result.add("".join(curr_res))
                    self.max_len = len(curr_res)
                elif len(curr_res) == self.max_len:
                    self.result.add("".join(curr_res))
        else:
            if input[index] == "(":
                curr_res.append(input[index])
                self.dfs(input, index + 1, curr_res, left + 1, right)
                curr_res.pop()

                self.dfs(input, index+1, curr_res, left, right)
            elif input[index] == ")":
                self.dfs(input, index+1, curr_res, left, right)
                if left > right:
                    curr_res.append(input[index])
                    self.dfs(input, index+1, curr_res, left, right+1)
                    curr_res.pop()
            else:
                curr_res.append(input[index])
                self.dfs(input, index+1, curr_res, left, right)
                curr_res.pop()
        return

assert Solution().removeInvalidParentheses(")(f") == ["f"]
assert Solution().removeInvalidParentheses("()())()") == ["(())()","()()()"]