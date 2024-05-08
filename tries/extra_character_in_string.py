#https://leetcode.com/problems/extra-characters-in-a-string/
from typing import List
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordDictionary = WordDictionary()
        for word in dictionary:
            wordDictionary.addWord(word)
        node = wordDictionary.root
        count = 0
        for char in s:
            if node.is_word:
                node = wordDictionary.root
            if char not in node.children:
                count += 1
                node = wordDictionary.root
            else:
                node = node.children[char]
        return count

assert Solution().minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"]) == 1
assert Solution().minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"]) == 3
