class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        def change(row, col):
            for i in range(m):
                if matrix[i][col] == 0:
                    continue
                matrix[i][col] = '#'
            for i in range(n):
                if matrix[row][i] == 0:
                    continue
                matrix[row][i] = '#'

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    change(i,j)

        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
        