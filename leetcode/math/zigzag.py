#https://leetcode.com/problems/zigzag-conversion/solutions/3133966/easy-explanation-with-pics-and-video-java-c-python/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lenstring=len(s)
        result = ""
        diff = 2 * (numRows -1)
        intermediate_diff = diff
        index = 0
        for i in range(numRows):
            index = i
            while index < lenstring:
                result += s[index]
                if i != 0 and i != numRows-1:
                    intermediate_diff = diff - 2*i
                    subsequent_diff = index + intermediate_diff
                    if subsequent_diff < lenstring:
                        result += s[subsequent_diff]
                index += diff
        return result

assert Solution().convert(s = "PAYPALISHIRING", numRows = 3) == "PAHNAPLSIIGYIR"
assert Solution().convert(s = "PAYPALISHIRING", numRows = 4) == "PINALSIGYAHRPI"
assert Solution().convert(s = "A", numRows = 1) == "A"

                
