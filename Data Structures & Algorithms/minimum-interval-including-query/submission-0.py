from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by left endpoint
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)

        # Pair each query with its original index, then sort by query value
        indexed_queries = sorted([(q, i) for i, q in enumerate(queries)])

        ans = [-1] * len(queries)
        heap = []  # min-heap of (length, right)
        i = 0      # pointer over intervals

        for q, idx in indexed_queries:
            # Add all intervals that start on/before q
            while i < n and intervals[i][0] <= q:
                L, R = intervals[i]
                heapq.heappush(heap, (R - L + 1, R))
                i += 1

            # Remove intervals that end before q (can't cover q)
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # Top of heap (if any) is the shortest interval covering q
            if heap:
                ans[idx] = heap[0][0]  # the length

        return ans
