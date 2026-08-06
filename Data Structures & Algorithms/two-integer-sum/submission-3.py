class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #approach 1: using 2 for loops
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
        
