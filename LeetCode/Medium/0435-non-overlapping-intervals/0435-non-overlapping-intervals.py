class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # whole = [float('inf'), float('-inf')]
        remove = 0
        prev_end = float('-inf')

        for start, end in intervals:
            # overlap
            if start < prev_end:
                remove += 1
                # abandon
                if end > prev_end:
                    continue
                # print(start, end)
            prev_end = end
        return remove