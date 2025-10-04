from collections import deque
class Solution:
    def simplifyPath(self, cwd: str, cd:str) -> str:
        stack = deque()
        stack = [char for char in cwd.split("/") if char]
        if cd.startswith("/"):
            stack = []
        tokens = cd.split("/")
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

assert Solution().simplifyPath("/a/b/c", "./d/../e/") == "/a/b/c/e"