class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        
        def dfs(arr:List[int])->int:
            prev2,prev1=0,0
            for x in arr:
                curr = max(x+prev2,prev1)
                prev2,prev1=prev1,curr
            return prev1
        
        return max(dfs(nums[:-1]),dfs(nums[1:]))