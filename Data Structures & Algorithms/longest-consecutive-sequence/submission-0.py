class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest_strk=0

        for num in nums:
            if num-1 not in num_set:
                current_num=num
                current_strk=1


                while current_num+1 in num_set:
                    current_num+=1
                    current_strk+=1

                
                longest_strk=max(longest_strk,current_strk)
        return longest_strk