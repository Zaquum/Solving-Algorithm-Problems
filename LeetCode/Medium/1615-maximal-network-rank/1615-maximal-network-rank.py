class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n

        for road in roads:
            degrees[road[0]] += 1
            degrees[road[1]] += 1
        
        max_rank = 0
        for i in range(n):
            for j in range(i+1,n):
                rank = degrees[i] + degrees[j]
                if [i,j] in roads or [j,i] in roads:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank