from itertools import chain
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)
        if not Solution._ValidRows(board):
            return False
        if not Solution._ValidColumns(board):
            return False
        if not Solution._Valid3x3(board):
            return False
        return True
    
    @staticmethod
    def _Valid3x3(board)-> bool:
        i = 0
        j = 0
        for row in range(0,9,3):
            for col in range(0,9,3):
                temp3x3 = [board[row+drow][col+dcol] for drow in range(3) for dcol in range(3)]
                print("3x3 {0}".format(temp3x3))
                if not Solution._ValidNumbers(chain.from_iterable(zip(*temp3x3))):
                    return False
                j += 3
            i += 3
        return True

    @staticmethod
    def _ValidRows(board) -> bool:
        for i in range(len(board)):
            print("Rows {0}".format(board[i]))
            if not Solution._ValidNumbers(board[i]):
                print("False Row")
                return False
        return True

    @staticmethod
    def _ValidColumns(board) -> bool:
        for col in list(zip(*board)):
            print("Columns: {0}".format(col))
            if not Solution._ValidNumbers(col):
                print("False Col")
                return False
        return True

    @staticmethod
    def _ValidNumbers(numlist) -> bool:
        c={}
        for item in numlist:
            if item is ".":
                continue
            else:
                try:
                    c[item] -= 1
                except KeyError:
                    c[item] = 1
        return all(False if temp < 1 else True for temp in c.values() )

