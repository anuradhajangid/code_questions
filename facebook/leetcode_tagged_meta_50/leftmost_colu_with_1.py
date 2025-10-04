class BnaryMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def get (self, i, j):
        return self.matrix[i][j]
    
class Solution():
    def leftmostColumnWith1(matrix):
        row, col = BinaryMatric.getDimensions()
        cr = 0
        cc = col - 1
        while cr < row and cc >=0:
            if BinaryMatric.get(cr, cj) == 1:
                cc -=1
            else:
                cr += 1
        if cc != col -1:
            return cc + 1
        else:
            return  -1
        
