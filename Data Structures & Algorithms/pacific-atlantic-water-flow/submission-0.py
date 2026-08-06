class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return []
        m, n = len(heights), len(heights[0])
        pacific = [[False]*n for _ in range(m)]
        atlantic = [[False]*n for _ in range(m)]

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or r >= m or c < 0 or c >= n or
                visited[r][c] or heights[r][c] < prevHeight):
                return
            visited[r][c] = True
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r+dr, c+dc, visited, heights[r][c])

        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n-1, atlantic, heights[r][n-1])
        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m-1, c, atlantic, heights[m-1][c])

        result = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])

        return result
