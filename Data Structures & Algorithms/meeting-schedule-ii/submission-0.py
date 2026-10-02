"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        rooms = 0
        max_rooms = 0
        s, e = 0, 0

        for i in range(len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)
        
        starts.sort()
        ends.sort()

        while s < len(starts):
            if starts[s] < ends[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            max_rooms = max(max_rooms, rooms)
        return max_rooms
            
