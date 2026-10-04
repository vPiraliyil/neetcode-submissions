class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        kset = set()
        for i in range(len(nums)):
            kset.add(nums[i])

        unique = sorted(kset)
        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(kset)