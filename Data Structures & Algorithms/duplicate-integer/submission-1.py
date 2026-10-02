class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set()

        for i in range(len(nums)):
            numbers.add(nums[i])

        if len(numbers) < len(nums):
            return True
        else:
            return False