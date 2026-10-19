class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n-1] = 1

        stair = n - 2

        while stair >= 0:
            dp[stair] = dp[stair + 1] + dp[stair + 2] 
            stair -= 1
        
        return dp[0]

