class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(u,v) for u,v in edges)
        parent = [i for i in range(n+1)]

        rank = [0]*(n+1)

        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rx,ry = find(x),find(y)
            if rx==ry:
                return False
            if rank[rx]<rank[ry]:
                parent[rx]=ry
            elif rank[rx] > rank[ry]:
                parent[ry]=rx
            else:
                parent[ry]=rx
                rank[rx]+=1
            return True
        ans = None
        for u,v in edges:
            if not union(u,v):
                ans = [u,v]
        return ans