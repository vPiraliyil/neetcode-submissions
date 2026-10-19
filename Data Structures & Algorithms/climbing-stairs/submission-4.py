from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def ways(step):
            if step >= n-1:
                return 1
            
            if step in memo:
                return memo[step]
            memo[step] = ways(step + 1) + ways(step + 2)
            return memo[step]

        return ways(0)
            