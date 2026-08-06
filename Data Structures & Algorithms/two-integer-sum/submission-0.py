class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dct={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in num_dct:
                return [num_dct[diff],i]
            num_dct[num]=i