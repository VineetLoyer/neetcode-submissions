class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # approach 1: (Worst case)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True

        return False