class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i,x in enumerate(nums):
            if i>farthest:
                return False
            farthest = max(farthest,i+x)
            if farthest>=n-1:
                return True
        return farthest>=n-1