class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # n = len(nums) 
        # if n == 1: 
        #     return False 
        # dp = [True, False, nums[0] == nums[1] if n > 1 else False] 
        # for i in range(2, n): 
        #     current_dp = (nums[i] == nums[i-1] and dp[1]) or \
        #                  (nums[i] == nums[i-1] == nums[i-2] and dp[0]) or \
        #                  (nums[i] - nums[i-1] == 1 and nums[i-1] - nums[i-2] == 1 and dp[0])
        #     dp[0], dp[1], dp[2] = dp[1], dp[2], current_dp 
        # return dp[2]
        memo = {}
        
        def helper(start):
            if start >= len(nums):
                return True

            if start in memo:
                return memo[start]

            # Condition 1
            if start + 1 < len(nums) and nums[start] == nums[start + 1]:
                if helper(start + 2):
                    memo[start] = True
                    return True

            # Condition 2
            if start + 2 < len(nums) and nums[start] == nums[start + 1] == nums[start + 2]:
                if helper(start + 3):
                    memo[start] = True
                    return True

            # Condition 3
            if start + 2 < len(nums) and nums[start + 1] == nums[start] + 1 and nums[start + 2] == nums[start] + 2:
                if helper(start + 3):
                    memo[start] = True
                    return True

            memo[start] = False
            return False
        
        return helper(0)
