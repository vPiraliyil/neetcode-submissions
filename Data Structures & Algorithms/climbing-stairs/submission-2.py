class Solution:
    def climbStairs(self, n: int) -> int:
        one_above = 1
        two_above = 1
        res = 1

        stair = n - 2

        while stair >= 0: 
            res = one_above + two_above
            one_above = two_above
            two_above = res
            stair -= 1
        
        return res

