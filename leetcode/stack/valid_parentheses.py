#https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()
        charopen = ['(', '{', '[']
        charclose = [')', '}', ']']
        for char in s:
            if char in charclose:
                if len(dq):
                    if (not dq[-1] in charopen):
                        return False
                    if (char == charclose[0] and dq[-1] != charopen[0]) or (char == charclose[1] and dq[-1] != charopen[1]) or (char == charclose[2] and dq[-1] != charopen[2]):
                        return False
                else:
                    if char in charclose:
                        return False
                dq.pop()
            else:
                dq.append(char)
        if not dq:
            return True