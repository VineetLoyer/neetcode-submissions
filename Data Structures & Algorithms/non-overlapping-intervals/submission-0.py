class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return False
        intervals.sort(key=lambda x:x[0])
        removals=0
        end_keep = intervals[0][1]
        for s,e in intervals[1:]:
            if s<end_keep:
                removals+=1
                end_keep = min(end_keep,e)
            else:
                end_keep = e
        return removals