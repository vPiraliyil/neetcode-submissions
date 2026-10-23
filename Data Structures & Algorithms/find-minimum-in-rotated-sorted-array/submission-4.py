class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            middle = (right + left) // 2
            
            if nums[middle] > nums[right]:
                # in unsorted portion
                left = middle + 1
            
            else:
                #in sorted portion
                right = middle

        return nums[right]
    