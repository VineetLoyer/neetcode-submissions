class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = [] #result array
        self.backtrack([],nums,[False]*len(nums)) #start with empty res, and [False,...]
        return self.res

    def backtrack(self,perm:List[int],nums:[List],pick:List[int]):
        #base case: if permutation is complete I return 
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm,nums,pick)
                perm.pop()
                pick[i] = False