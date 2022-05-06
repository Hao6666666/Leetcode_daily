class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dris = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            for dx, dy in dris:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == '1':
                    grid[new_x][new_y] = '0'
                    dfs(new_x, new_y)

        cnt = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r, c)
                    cnt += 1
        return cnt