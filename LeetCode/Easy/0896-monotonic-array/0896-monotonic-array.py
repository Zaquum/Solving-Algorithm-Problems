class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i = 1
        j = 1
        while i < len(nums):
            if nums[i-1] <= nums[i]:
                i += 1
            else:
                break
        while j < len(nums):
            if nums[j-1] >= nums[j]:
                j += 1
            else:
                break
        return i == len(nums) or j == len(nums)