#https://leetcode.com/problems/word-search-ii/description/

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
    def __init__(self) -> None:
        self.grid = None
        self.rows = None
        self.cols = None
        self.trie = WordDictionary()
        

    def findWords(self, grid, words):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        for word in words:
            self.trie.addWord(word)

        result = []
        node = self.trie.root
        def dfs(i, j, visited, root):
            if root.is_word:
                result.append(visited)
                root.is_word = False
            if i < 0 or i >= len(board) or j < 0 or j >= len(self.grid[0]):
                return
            char = self.grid[i][j]
            if not char in root.children:
                return 
            curr = root.children[char]
            self.grid[i][j] = "$"
            dfs(i-1,j,visited+char,curr)
            dfs(i+1,j,visited+char,curr)
            dfs(i, j-1, visited+char, curr)
            dfs(i,j+1,visited+char,curr)
            self.grid[i][j] = char

        for i in range(self.rows):
            for j in range(self.cols):
                dfs(i, j, "", node)

        return result
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


