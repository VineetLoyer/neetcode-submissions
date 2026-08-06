from functools import lru_cache
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m,n = len(matrix),len(matrix[0])
        DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

        @lru_cache(None)
        def dfs(r:int,c:int)->int:
            best = 1
            cur = matrix[r][c]
            for dr,dc in DIRS:
                nr,nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>cur:
                    best = max(best,1+dfs(nr,nc))
            return best
        
        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans,dfs(r,c))
        return ans