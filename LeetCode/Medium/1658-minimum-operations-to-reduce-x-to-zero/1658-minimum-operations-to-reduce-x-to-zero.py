class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x

        if target < 0:
            return -1

        left = 0
        current_sum = 0
        max_length_subarray = -1

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_length_subarray = max(max_length_subarray, right - left + 1)

        if max_length_subarray == -1:
            return -1

        return len(nums) - max_length_subarray