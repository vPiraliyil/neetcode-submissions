import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        counter = Counter(nums)

        for num, freq in counter.items():
            if len(h) < k:
                heapq.heappush(h, (freq, num))
            else:
                heapq.heappushpop(h, (freq, num))

        return[t[1] for t in h]