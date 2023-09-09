class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # result = 0
        # def solve(n):
        #     nonlocal result
        #     if n > target:
        #         return
        #     if n == target:
        #         result += 1
        #     for num in nums:
        #         n += num
        #         solve (n)
        #         n -= num
        # solve(0)
        # return result
        dp = [0] * (target+1)
        dp[0] = 1
        
        for i in range(1, target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i-num]

        return dp[-1]