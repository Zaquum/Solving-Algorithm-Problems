class Solution:
    def minOperations(self, nums: List[int]) -> int:
        unique_sorted = sorted(list(set(nums)))
        n = len(nums)

        l, r, ans = 0, 0, 0

        while r < len(unique_sorted):
            while unique_sorted[r] - unique_sorted[l] >= n:
                l += 1

            ans = max(ans, r - l + 1)
            r += 1

        return n - ans