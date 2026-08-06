class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!= n-1:
            return False
        from collections import defaultdict

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor,node):
                    return False
            return True
        
        if not dfs(0,-1):
            return False
        
        return len(visited)==n