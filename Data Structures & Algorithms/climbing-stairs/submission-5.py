from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def ways(step):
            if step >= n-1:
                return 1
            return ways(step + 1) + ways(step + 2)
        return ways(0)
        