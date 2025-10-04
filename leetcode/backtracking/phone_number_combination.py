#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution(object):
    MAP = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if digits == "" :
            return []
        def backtrack(index, current):
            if index == len(digits):
                result.append("".join(current))
                return
            for char in self.MAP[digits[index]]:
                current.append(char)
                if index < len(digits):
                    backtrack(index+1, current)
                    current.pop()
        backtrack(0,[])
        return result

            
s= Solution()
assert s.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
assert s.letterCombinations("") ==[]
assert s.letterCombinations("2") == ["a","b","c"]  