class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0 
        q = deque()
        visited = set()

        rows, cols = len(grid), len(grid[0])

        moves = [ [-1, 0], [1, 0], [0, 1], [0, -1] ]

        def bfs(x, y):
            for move in moves:
                newX = move[0] + x 
                newY = move[1] + y 

                if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == "1" and (newX, newY) not in visited: 
                    q.append( (newX, newY) )
                    visited.add( (newX, newY) )

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    q.append( (i, j) )
                    num += 1
                    visited.add( (i, j) )
                    while q: 
                        x, y = q.popleft()
                        bfs(x, y)
        
        return num