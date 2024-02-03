#https://www.educative.io/courses/grokking-coding-interview-patterns-python/solution-n-queens
class NQueen:
    def __init__(self, n) -> None:
        self.n = n
    @staticmethod
    def isValidMove(row, col, solution):
        for i in range (0, row):
            old_row = i 
            old_col = solution[i]
            diagonal = row - old_row
            if (old_col == col) or (old_col == col - diagonal) or (old_col == col + diagonal):
                return False
        return True

    def recursivelyFindBoardSolution(result, solution, n, row):
        if n == row:
            result.append(solution[:])
            return
        for i in range(n):
            if NQueen.isValidMove(row, i, solution):
                solution[row] = i
                NQueen.recursivelyFindBoardSolution(result, solution, n, row+1)

    
    def findBoardSolutions(self):
        solution  = [-1] * self.n
        result = []
        NQueen.recursivelyFindBoardSolution(result, solution, self.n, 0)
        return (len(result), result)

        
    
    def postProcess(self, solution):
        result = []
        for sol in solution:
            rows = []
            for data in sol:
                temp = ["."] * self.n
                temp[data] = "Q"
                rows.append("".join(temp))
            result.append(rows)
        return result



                
queen = NQueen(4)
len, sol = queen.findBoardSolutions()
print(len, sol)
print (queen.postProcess(sol))
