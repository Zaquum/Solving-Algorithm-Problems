class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        vector<pair<int,int>> directions = {{1,0},{0,1}};
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        if(obstacleGrid[m-1][n-1]==1)
            return 0;
        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[0][0] = 1;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(obstacleGrid[i][j]!=1){
                    for(int k=0;k<directions.size();k++){
                        if(i+directions[k].first>=m || j+directions[k].second>=n)
                            continue;
                        dp[i+directions[k].first][j+directions[k].second] += dp[i][j];
                    }
                }
            }
        }
        return dp[m-1][n-1];
    }
};