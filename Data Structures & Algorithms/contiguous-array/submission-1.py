class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = dict()
        prefix[0] = -1
        currsum = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                currsum += -1
            else:
                currsum += 1

            if currsum in prefix:
                res =max(res, i - prefix[currsum])
            else:
                prefix[currsum] = i
        return res
