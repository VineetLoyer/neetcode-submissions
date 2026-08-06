class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10**15
        dp = [INF]*n
        dp[src] = 0
        for _ in range(k+1):
            next_dp = dp[:]
            for u,v,w in flights:
                if dp[u]!=INF and dp[u]+w<next_dp[v]:
                    next_dp[v]=dp[u]+w
            dp = next_dp
        return -1 if dp[dst]==INF else dp[dst]