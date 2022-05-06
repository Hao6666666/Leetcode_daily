class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [x for x in range(26)]
        rank = [1 for _ in range(26)]

        def find(x):  # 路经压缩
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            a = find(x)  # find parent of x
            b = find(y)  # find parent of y
            if a == b:
                return
            elif rank[a] > rank[b]:  # 按秩合并
                parent[b] = a
            elif rank[b] > rank[a]:
                parent[a] = b
            else:
                parent[a] = b
                rank[b] += 1

        for c in equations:
            if c[1] == '!':
                continue
            a = ord(c[0]) - ord('a')
            b = ord(c[3]) - ord('a')
            union(a, b)

        for c in equations:
            if c[1] == '=':
                continue
            a = ord(c[0]) - ord('a')
            b = ord(c[3]) - ord('a')
            if find(a) == find(b):
                return False
        return True
