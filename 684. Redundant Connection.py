class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [c for c in range(len(edges) + 1)]
        rank = [1 for _ in range(len(edges) + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            if a == b:
                return
            elif rank[a] > rank[b]:
                parent[b] = a
            elif rank[a] < rank[b]:
                parent[a] = b
            else:
                parent[a] = b
                rank[b] += 1

        for a, b in edges:
            # if a and b has the same parent node
            # this edges froms a cycle in graph which is redundant
            if find(a) == find(b):
                return [a, b]
            else:
                union(a, b)
