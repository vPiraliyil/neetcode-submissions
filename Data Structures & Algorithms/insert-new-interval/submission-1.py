class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(0, len(intervals)):
            curr_start, curr_end = intervals[i]
            new_start, new_end = newInterval
            
            if  curr_end < new_start:
                result.append([curr_start, curr_end])
            elif curr_start > new_end:
                result.append([new_start, new_end])
                newInterval = [curr_start, curr_end]
            else :
                newInterval[0] = min(newInterval[0], curr_start)
                newInterval[1] = max(newInterval[1], curr_end)

        result.append(newInterval)
            

        return result