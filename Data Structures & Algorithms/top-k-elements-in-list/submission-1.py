class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq_dict=Counter(nums)
        # heap=[]
        # for num,freq in freq_dict.items():
        #     heapq.heappush(heap,(freq,num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # return [item[1] for item in heap]
        #Solution 2: sorting all elements
        freq=Counter(nums) #{1:1,2:2,3:3}
        sorted_items=sorted(freq.items(),key =lambda x:x[1],reverse=True) # sort in descending order of freq 
        # sorted_items:{3:3,2:2,1:1}
        return [item for item,count in sorted_items[:k]]