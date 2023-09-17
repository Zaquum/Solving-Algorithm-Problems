class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<vector<int>> dist(n, vector<int>(n, n)); // 4x4
        vector<vector<int>> dp(1 << n, vector<int>(n, n * n)); // 16x4
        // cout << dp.size() << " " << dp[0].size();

        // Initialize the distance matrix and dp array
        for(int i = 0; i < n; ++i) {
            dist[i][i] = 0;
            dp[1 << i][i] = 0;
            for(int j : graph[i]) {
                dist[i][j] = 1;
            }
        }

        // Floyd-Warshall Algorithm to find shortest distances between every pair of vertices
        for(int k = 0; k < n; ++k) {
            for(int i = 0; i < n; ++i) {
                for(int j = 0; j < n; ++j) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        // Dynamic programming to find the shortest path that visits every node
        for(int mask = 1; mask < (1 << n); ++mask) {
            for(int u = 0; u < n; ++u) {
                for(int v = 0; v < n; ++v) {
                    if((mask & (1 << v)) == 0) {
                        dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + dist[u][v]);
                    }
                }
            }
        }

        // Finding the minimum length of the path that visits every node
        int res = n * n;
        for(int i = 0; i < n; ++i) {
            res = min(res, dp[(1 << n) - 1][i]);
        }

        return res;
    }
};