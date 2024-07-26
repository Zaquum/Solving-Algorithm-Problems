class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
    
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        min_reachable_cities = float('inf')
        best_city = -1

        for i in range(n):
            reachable_cities = sum(dist[i][j] <= distanceThreshold for j in range(n))

            if reachable_cities <= min_reachable_cities:
                min_reachable_cities = reachable_cities
                best_city = i

        return best_city