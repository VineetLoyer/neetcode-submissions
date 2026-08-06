class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result= []
        start=0
        end=k-1

        while end<len(nums):
            current_max = max(nums[start:end+1])
            result.append(current_max)
            start+=1
            end+=1
        
        return result