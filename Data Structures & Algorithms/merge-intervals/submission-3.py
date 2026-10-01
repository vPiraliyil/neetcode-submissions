class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_start, prev_end = result[-1]
            curr_start, curr_end = intervals[i]

            if curr_start <= prev_end:
                result[-1][1] = max(prev_end, curr_end)
            else:
                result.append([curr_start, curr_end])

        return result