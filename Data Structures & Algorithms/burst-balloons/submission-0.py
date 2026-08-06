class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)
        dp = [[0]*n for _ in range(n)]

        for length in range(2,n):
            for l in range(0,n-length):
                r = l+length
                best= 0
                for k in range(l+1,r):
                    best = max(best,arr[l]*arr[k]*arr[r]+dp[l][k]+dp[k][r])
                dp[l][r] = best
        return dp[0][n-1]