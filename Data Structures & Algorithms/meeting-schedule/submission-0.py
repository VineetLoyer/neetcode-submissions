"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        prev_end = float('-inf')
        for iv in intervals:
            if iv.start < prev_end:
                return False
            prev_end = iv.end
        return True

