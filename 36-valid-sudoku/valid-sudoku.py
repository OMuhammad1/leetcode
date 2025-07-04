class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sq = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j] 
                box = (i // 3) * 3 + (j // 3) 

                if num == '.':
                    continue 
                
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False 
                if num in sq[box]:
                    return False 
                
                rows[i].add(num)
                cols[j].add(num)
                sq[box].add(num)
        
        return True
                

        