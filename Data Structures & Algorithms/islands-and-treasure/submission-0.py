from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        TREASURE = 0
        LAND  = pow(2,31)-1
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r,c))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r,c = queue.popleft()
            for nr,nc in directions:
                row = r+nr
                col = c+nc
                if 0<=row<ROW and 0<=col<COL and grid[row][col]==LAND:
                    grid[row][col] = grid[r][c]+1
                    queue.append((row,col))
        


            
