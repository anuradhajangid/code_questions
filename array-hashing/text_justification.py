#https://leetcode.com/problems/text-justification/
from typing import List
import math
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        lenline = 0
        for word in words:
            if lenline + len(line) + len(word)> maxWidth:
                for space in range(maxWidth - lenline):
                    line[space % (len(line)-1 or 1)] += " "
                result.append("".join(line))
                line = []
                lenline = 0
            line.append(word)
            lenline += len(word)
        return result + [' '.join(line).ljust(maxWidth)]        



assert Solution().fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16) == [
   "This    is    an",
   "example  of text",
   "justification.  "
]

assert Solution().fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16) == [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
assert Solution().fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20) == [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]