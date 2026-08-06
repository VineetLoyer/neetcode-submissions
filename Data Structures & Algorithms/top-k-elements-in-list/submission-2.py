class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       #Best Solution: using Heap 
       freq=Counter(nums)
       return[item for item,count in heapq.nlargest(k,freq.items(),key=lambda x:x[1])]

        # #Solution 2: sorting all elements O(n+mlogm) mlogm for sorting, n for counting TC, O(n) SC
        # freq=Counter(nums) #{1:1,2:2,3:3}
        # sorted_items=sorted(freq.items(),key =lambda x:x[1],reverse=True) # sort in descending order of freq 
        # # sorted_items:{3:3,2:2,1:1}
        # return [item for item,count in sorted_items[:k]] #sorted[:k] slices the list using k
        # #item for item,count .. extract item from (item,freq) in list