class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum = 0
        res = 0
        prefix = {}

        for num in nums:
            currsum += num

            if currsum == k:
                res += 1

            if currsum - k in prefix:
                res += prefix[currsum - k]
            
            if currsum in prefix:
                prefix[currsum] += 1
            else:
                prefix[currsum] = 1
        return res

        