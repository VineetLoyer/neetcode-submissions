"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x.start)
        ends = []
        for i in intervals:
            if ends and i.start >=ends[0]:
                heapq.heappop(ends)
            heapq.heappush(ends,i.end)
        return len(ends)