class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        n = len(nums)
        total_ones = sum(nums)

        if total_ones == 0 or total_ones == n:
            return 0

        extended_nums = nums * 2

        current_ones = sum(extended_nums[:total_ones])
        max_ones_in_window = current_ones

        for i in range(1, n):
            current_ones = current_ones - extended_nums[i - 1] + extended_nums[i + total_ones - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones)

        min_swaps = total_ones - max_ones_in_window
        return min_swaps