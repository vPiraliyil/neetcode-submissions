class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {} #sum, times
        res = 0
        currsum = 0

        if not nums:
            return 0

        for num in nums:
            currsum += num

            if currsum == k:
                res += 1

            if currsum - k in prefix:
                res += prefix[currsum - k]

            if currsum not in prefix:
                prefix[currsum] = 1
            else:
                prefix[currsum] += 1
        return res            
