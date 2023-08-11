class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = [0] * (amount+1)
        # dp[0] = 1
        
        # for coin in coins:
        #     for i in range(1,amount+1):
        #         if i-coin >= 0:
        #             dp[i] += dp[i-coin]
        # return dp[amount]
        memo = {}

        def dfs(remaining, start):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            if (remaining, start) in memo:
                return memo[(remaining, start)]

            ans = 0
            for i in range(start, len(coins)):
                ans += dfs(remaining - coins[i], i)

            memo[(remaining, start)] = ans
            return ans

        return dfs(amount, 0)