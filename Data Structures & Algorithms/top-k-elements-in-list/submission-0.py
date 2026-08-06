class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict=Counter(nums)
        heap=[]
        for num,freq in freq_dict.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [item[1] for item in heap]