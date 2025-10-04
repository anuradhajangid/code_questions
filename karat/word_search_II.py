from typing import List
import attrs

class Trinode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

    def addWord(self, word):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = Trinode()
            current = current.children[c]
        current.isWord = True

class Solution:
    def exist(self, board: List[List[str]], words: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        res = set()

        root = Trinode()
        for w in words:
            root.addWord(w)
        
        def dfs(r, c, node:Trinode, word:str):
            if r < 0 or c < 0 or r>=ROWS or c>=COLS or (r,c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r,c))            
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c))

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,root,"")
        return list(res)
    
assert Solution().exist(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]) == ["eat","oath"]
