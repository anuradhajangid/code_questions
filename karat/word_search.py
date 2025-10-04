from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board)
        M = len(board[0])

        def dfs(i,j,index):
            nonlocal M
            nonlocal N
            nonlocal board
            nonlocal word

            if index == len(word) - 1:
                return True
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dir in directions:
                newi, newj = i + dir[0], j + dir[1]
                if 0 <= newi < N and 0 <= newj < M and board[newi][newj] == word[index+1]:
                    board[i][j] = "*"
                    if dfs(newi,newj,index+1):
                        return True
                    board[i][j] = word[index]
            return False

            
        
        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False