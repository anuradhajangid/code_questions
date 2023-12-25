#https://leetcode.com/problems/generate-parentheses/description/
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Recursive approach
        def _recurse(left, right, leaf):
            if len(leaf) == n*2:
                permutations.append(leaf)
                return

            if left < n:
                _recurse(left+1, right, leaf+"(")
            
            if right< left:
                _recurse(left, right+1, leaf+")")

        permutations = []
        _recurse(0,0,"")
        return permutations
                    
            

            
            