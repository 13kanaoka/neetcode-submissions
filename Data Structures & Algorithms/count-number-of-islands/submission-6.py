class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return
            if grid[row][col] == "0" or grid[row][col] == "-1":
                return

            grid[row][col] = "-1"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
                elif grid[row][col] == "-1" or grid[row][col] == "0":
                    continue

        return count