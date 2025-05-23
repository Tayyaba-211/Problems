class Solution:
    def findRightInterval(self, intervals):
        # Map start times to their indices
        start_times = sorted((interval[0], i) for i, interval in enumerate(intervals))
        starts = [s for s, _ in start_times]
        result = []

        for interval in intervals:
            end = interval[1]
            idx = bisect_left(starts, end)
            if idx < len(intervals):
                result.append(start_times[idx][1])
            else:
                result.append(-1)

        return result