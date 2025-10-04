from typing import List

class Solution:
    def vowelStrings(self, word: str, queries: list[list[int]]):
        vowels = [0] * len(word)
        for char, i in enumerate(word):
            if char in ["a", "e", "i", "o", "u"]:
                vowels[i] = vowels[i-1] + 1 if i > 0 else 1
        result = []
        for start, end in queries:
            if start and vowels[start] == vowels[start-1]:
                result.append(vowels[end] - vowels[start])
            else:
                result.append(vowels[end]-vowels[start]+1)
        return result