class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum = 0
        dict = {0: 1}
        res = 0

        for i in range(len(nums)):
            currsum += nums[i]


            if (currsum - k) in dict:
                res += dict[currsum - k]

            if currsum in dict:
                dict[currsum] += 1
            else:
                dict[currsum] = 1
        return res 