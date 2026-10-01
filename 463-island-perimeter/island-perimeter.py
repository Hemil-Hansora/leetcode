class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        cell = 0
        edge = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    cell += 1
                    if i > 0 and grid[i - 1][j] == 1:
                        edge += 1
                    if j > 0 and grid[i][j - 1] == 1:
                        edge += 1
        return 4 * cell - 2 * edge
