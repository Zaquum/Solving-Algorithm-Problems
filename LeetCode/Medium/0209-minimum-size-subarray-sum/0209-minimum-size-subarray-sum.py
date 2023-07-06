class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0
        
        ans = float('inf')
        start = 0
        end = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                ans = min(ans, i - start + 1)
                total -= nums[start]
                start += 1
        return ans if ans != float('inf') else 0
