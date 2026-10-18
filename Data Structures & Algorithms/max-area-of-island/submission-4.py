class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def DFS(r, c)-> int: 
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):

                if grid[r][c] == 0:
                    return 0

                if grid[r][c] == 1:
                    grid[r][c] = 0
                    return 1 + DFS(r+1, c) + DFS(r, c+1) + DFS(r, c-1) + DFS(r-1, c)
            return 0
               
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count = 0
                    area = DFS(r, c)
                    res = max(area, res)
        return res

                