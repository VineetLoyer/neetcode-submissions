class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        merged = []
        curL,curR = intervals[0]
        for start, end in intervals[1:]:
            if start<=curR:
                curR = max(curR,end)
            else:
                merged.append([curL,curR])
                curL,curR = start,end
        merged.append([curL,curR])
        return merged