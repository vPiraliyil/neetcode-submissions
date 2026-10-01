class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        
        running_product = 1
        for i in range(len(nums)):
            prefix[i] = running_product
            running_product *= nums[i]

        running_product = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = running_product
            running_product *= nums[i]

        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result