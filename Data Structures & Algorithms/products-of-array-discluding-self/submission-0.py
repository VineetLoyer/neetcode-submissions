class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[]
        for i in range(n):
            prd=1
            for j in range(n):
                if i!=j:
                    prd*=nums[j]
            output.append(prd)
        return output