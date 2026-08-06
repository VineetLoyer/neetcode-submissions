class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Best solution - O(n) TC and O(n) SC
        num_dict ={}
        for i, num in enumerate(nums):
            diff=target-num
            if diff in num_dict:
                return [num_dict[diff],i]
            num_dict[num]=i
            
        # O(n^2) solution
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return []