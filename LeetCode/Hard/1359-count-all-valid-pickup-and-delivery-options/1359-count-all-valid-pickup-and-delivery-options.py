class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        
        def dp(n: int)->int:
            if n==1:
                return 1
            if n in memo:
                return memo[n]
            
            count = (dp(n-1) * (2 * n - 1) * n) % MOD
            memo[n] = count
            return count

        return dp(n)
