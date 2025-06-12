class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

        for k in range(n):
            #matrix[k].reverse()
            for l in range(n//2):
                matrix[k][l], matrix[k][n - 1 - l] = matrix[k][n - 1 -l], matrix[k][l]
        

        




        