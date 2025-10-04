#https://leetcode.com/problems/simplify-path/description/?envType=problem-list-v2&envId=7p59281
from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        tokens = path.split("/")
        for token in tokens:
            if token == "" or token == ".":
                continue
            if token == "..":
                if stack:
                    stack.pop()
                continue
            else:
                stack.append(token)
        return "/" +"/".join(stack)

assert Solution().simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"
assert Solution().simplifyPath("/.../ab/") == "/.../ab"
assert Solution().simplifyPath("/") == "/"
            