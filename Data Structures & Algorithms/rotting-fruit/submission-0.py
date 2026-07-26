from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        fresh_oranges = 0
        ROW = len(grid)
        COL = len(grid[0])
        SOURCE = 2
        FRESH = 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        time=0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == SOURCE:
                    visited.add((r,c))
                    queue.append((r,c))
                if grid[r][c] == FRESH:
                    fresh_oranges+=1
        while queue and fresh_oranges>0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    row = r+dr
                    col = c+dc
                    if 0<=row<ROW and 0<=col<COL and (row,col) not in visited and grid[row][col] == FRESH:
                        queue.append((row,col))
                        visited.add((row,col))
                        fresh_oranges-=1
            time+=1
        print("time: ",time)
        return time if fresh_oranges==0 else -1
                
        