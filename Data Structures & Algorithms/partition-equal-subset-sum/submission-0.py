class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2==1:
            return False
        target  = s//2
        dp = [False]*(target+1)
        dp[0] = True
        for x in nums:
            for s in range(target,x-1,-1):
                dp[s] = dp[s] or dp[s-x]
            if dp[target]:
                return True
        return dp[target]