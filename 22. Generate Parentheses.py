class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(leftP, rightP, cnt, path):
            if leftP == rightP == 0:
                res.append(path)
            if leftP > 0:
                dfs(leftP - 1, rightP, cnt + 1, path + '(')
            if rightP > 0 and cnt > 0:  # cnt > 0 避免出现反括号
                dfs(leftP, rightP - 1, cnt - 1, path + ')')

        dfs(n, n, 0, '')
        return res
