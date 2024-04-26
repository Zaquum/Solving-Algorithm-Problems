class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = grid[i][j]
                else:
                    min_dp = float('inf')
                    for k in range(m):
                        if k != j:
                            min_dp = min(min_dp, dp[i-1][k])
                    dp[i][j] = min_dp + grid[i][j]
        return min(dp[-1])