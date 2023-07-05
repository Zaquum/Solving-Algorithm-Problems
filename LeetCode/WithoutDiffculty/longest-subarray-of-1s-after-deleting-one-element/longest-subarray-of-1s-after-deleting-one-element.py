class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, zero_count, max_length = 0, 0, 0, 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

            right += 1

        return max_length - 1 if max_length == len(nums) else max_length - 1