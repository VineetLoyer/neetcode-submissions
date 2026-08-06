class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = [0]*len(nums)
        for i in range(len(nums)):
            new[i] = nums[i]
        return (nums+new)