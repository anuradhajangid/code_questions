#https://leetcode.com/problems/word-search-ii/description/
from typing import List
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def addWord(self, word):
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                current.children[char] = TrieNode()
                current = current.children[char]
        current.is_word = True

class Solution:
    def __init__(self) -> None:
        self.word_dict = WordDictionary()
        self.grid = None
        

    def findWords(self, grid: List[List], words: List[str]) -> List[str]:
        self.grid = grid
        node = self.word_dict.root
        for word in words:
            self.word_dict.addWord(word)

        result = []
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                self._backtrack(row, col, "", node, result)
        return result
    
    def _backtrack(self, row: int, col: int, current: str, node: TrieNode, result: List):
        if node.is_word:
            result.append(current)
            node.is_word = False
            return 
        if (row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[0])):
            return
        temp = self.grid[row][col]
        if not temp in node.children:
            return 
        node = node.children[temp]
        self.grid[row][col] = "$"
        for r,c in [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]:
            self._backtrack(r, c, current+ temp, node, result)
        self.grid[row][col] = temp


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]   
s = Solution()
print(s.findWords(board, words))             

board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]
s = Solution()
print(s.findWords(board, words))

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain","hklf", "hf"]
s = Solution()
print(s.findWords(board, words))


