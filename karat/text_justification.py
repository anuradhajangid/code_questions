from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        lines = []
        linelen = 0
        for word in words:
            if linelen + len(line) + len(word) > maxWidth:
                for space in range(maxWidth - linelen):
                    line[space % (len(line)-1 or 1)] += " "
                lines.append("".join(line))
                line = []
                linelen = 0
            line.append(word)
            linelen += len(word)
        
        if line:
            line.append(" " * (maxWidth - linelen - len(line)) if (linelen - len(line)) < maxWidth else "")
            lines.append(" ".join(line))
        return lines

assert Solution().fullJustify(words = ["this"], maxWidth= 8) == ["this    "]
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