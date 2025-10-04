from typing import List
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        wordsLen = 0
        charsFerq = Counter(chars)
        for word in words:
            wordFreq = Counter(word)
            wordExists = True
            for key, value in wordFreq.items():
                if key not in charsFerq or value > charsFerq[key]:
                    wordExists = False
                    break
            wordsLen += len(word) if wordExists else 0
        return wordsLen

        
                