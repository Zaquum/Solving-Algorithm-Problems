class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # From GPT
        
        import sys
        INF = sys.maxsize

        # Create a cost matrix initialized to INF
        n = 26  # Number of lowercase English letters
        cost_matrix = [[INF] * n for _ in range(n)]

        # Set the cost of transforming a character to itself to 0
        for i in range(n):
            cost_matrix[i][i] = 0

        # Populate the cost matrix with the given transformations
        for i in range(len(original)):
            orig = ord(original[i]) - ord('a')
            chng = ord(changed[i]) - ord('a')
            cost_matrix[orig][chng] = min(cost_matrix[orig][chng], cost[i])

        # Floyd-Warshall algorithm to find the shortest path between every pair of characters
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if cost_matrix[i][j] > cost_matrix[i][k] + cost_matrix[k][j]:
                        cost_matrix[i][j] = cost_matrix[i][k] + cost_matrix[k][j]

        # Calculate the total minimum cost to convert source to target
        total_cost = 0
        for i in range(len(source)):
            src_char = ord(source[i]) - ord('a')
            tgt_char = ord(target[i]) - ord('a')
            if cost_matrix[src_char][tgt_char] == INF:
                return -1  # Transformation is impossible
            total_cost += cost_matrix[src_char][tgt_char]

        return total_cost