class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(r, c, pos):
            if len(word) == pos:
                return True
            if 0 <= r < row and 0 <= c < col and board[r][c] == word[pos]:
                temp = board[r][c]
                board[r][c] = None
                res = dfs(r + 1, c, pos + 1) or dfs(r - 1, c, pos + 1) or dfs(r, c + 1, pos + 1) or dfs(r, c - 1,
                                                                                                        pos + 1)
                board[r][c] = temp

                return res
            else:
                return False

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False