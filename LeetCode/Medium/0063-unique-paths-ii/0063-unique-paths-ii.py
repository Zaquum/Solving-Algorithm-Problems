class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        directions = [(1,0),(0,1)]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0
            
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 1:
                    for y,x in directions:
                        if i+y < m and j+x < n:
                            dp[i+y][j+x] += dp[i][j]

        return dp[m-1][n-1]