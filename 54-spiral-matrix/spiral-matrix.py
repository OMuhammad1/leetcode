class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        size = m*n

        left = 0 
        top = 1
        right = m - 1
        bottom = n - 1
        x,y = 0, 0
        res = []

        while len(res) < size - 1:

            while y < right:
                res.append(matrix[x][y])
                y += 1
            right -= 1
            
            if len(res) >= size - 1:
                break
            
            while x < bottom:
                res.append(matrix[x][y])
                x += 1
            bottom -= 1
            
            if len(res) >= size - 1:
                break
            
            while y > left:
                res.append(matrix[x][y])
                y -= 1
            left += 1

            if len(res) >= size - 1:
                break

            while x > top:
                res.append(matrix[x][y])
                x -= 1
            top += 1

            if len(res) >= size - 1:
                break
            
        res.append(matrix[x][y])

        return res



        