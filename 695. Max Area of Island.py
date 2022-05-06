class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                grid[r][c] = 0
                self.cnt += 1

                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

            return self.cnt

        maxA = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    self.cnt = 0
                    cur = dfs(r, c)
                    maxA = max(maxA, self.cnt)
        return maxA