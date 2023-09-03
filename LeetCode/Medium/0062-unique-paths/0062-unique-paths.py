class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        # dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j ==0:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]