int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize){
    int directions[2][2] = {{1, 0}, {0, 1}};
    int m = obstacleGridSize;
    int n = obstacleGridColSize[0];
    if (obstacleGrid[m - 1][n - 1] == 1) {
        return 0;
    }

    int dp[m][n];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            dp[i][j] = 0;
        }
    }
    dp[0][0] = 1;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (obstacleGrid[i][j] != 1) {
                for (int k = 0; k < 2; ++k) {
                    int y = directions[k][0];
                    int x = directions[k][1];
                    if (i + y < m && j + x < n) {
                        dp[i + y][j + x] += dp[i][j];
                    }
                }
            }
        }
    }
    return dp[m-1][n-1];
}