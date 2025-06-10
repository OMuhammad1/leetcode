class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low, high = 0, rows - 1

        targetRow = None

        while low <= high:
            mid = (low + high) // 2

            if matrix[mid][0] > target: 
                high = mid - 1
            elif matrix[mid][0] < target:
                if matrix[mid][cols - 1] < target:
                    low = mid + 1 
                elif matrix[mid][cols - 1] > target: 
                    targetRow = matrix[mid]
                    break
                else:
                    return True
            else:
                return True 

        if not targetRow:
            return False
        
        low, high = 0, cols - 1

        while low <= high:
            mid = (low + high) // 2

            if targetRow[mid] > target:
                high = mid - 1
            elif targetRow[mid] < target:
                low = mid + 1
            else:
                return True
        
        return False 
        