class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # output=[]
        # for i in range(n):
        #     prd=1
        #     for j in range(n):
        #         if i!=j:
        #             prd*=nums[j]
        #     output.append(prd)
        # return output
        n=len(nums)
        output=[1]*n
        prefix_prd=1
        for i in range(n):
            output[i]=prefix_prd
            prefix_prd*=nums[i]
        
        suffix_prd=1
        for i in range(n-1,-1,-1):
            output[i]*=suffix_prd
            suffix_prd*=nums[i]
        
        return output