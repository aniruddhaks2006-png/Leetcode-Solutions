class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for row in matrix:
            if len(set(row))!=len(row):
                return False
        
        for l in range(len(matrix)):
            col=[]
            for row in matrix:
                col.append(row[l])
            if len(col)!=len(set(col)):
                return False
        return True


