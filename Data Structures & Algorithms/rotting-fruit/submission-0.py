from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r, c])
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        

        while queue and fresh_oranges > 0:
            minutes += 1
            oranges_now = len(queue)

            for _ in range(oranges_now):
                r, c = queue.popleft()
            
                for dr, dc in [(1, 0), (-1, 0), (0, +1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append([nr, nc])
        if fresh_oranges:
            return -1
        else:
            return minutes

