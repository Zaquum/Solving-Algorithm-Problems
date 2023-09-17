class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        
        for i, neighbors in enumerate(graph):
            for neighbor in neighbors:
                dist[i][neighbor] = 1
        
        # Floyd-Warshall algorithm to find the shortest distance between every pair of nodes
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Dynamic programming to find the shortest path that visits every node
        dp = [[float('inf')] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 0

        for mask in range(1, 1 << n):
            for u in range(n):
                if mask & (1 << u):
                    for v in range(n):
                        if mask & (1 << v) == 0:
                            dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + dist[u][v])
        
        return min(dp[(1 << n) - 1])