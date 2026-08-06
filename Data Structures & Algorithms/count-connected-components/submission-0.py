class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rootX,rootY = find(x),find(y)
            if rootX!=rootY:
                parent[rootY] = rootX
        for u,v in edges:
            union(u,v)

        return len(set(find(i) for i in range(n))) 