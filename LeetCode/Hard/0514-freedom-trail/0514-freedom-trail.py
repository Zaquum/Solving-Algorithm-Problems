class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos_map = defaultdict(list)
        for index, char in enumerate(ring):
            pos_map[char].append(index)

        n = len(ring)
        m = len(key)
        dp = [[float('inf')] * n for _ in range(m)]

        
        for i in pos_map[key[0]]:
            dp[0][i] = min(i, n - i) + 1  

        for i in range(1, m):
            for j in pos_map[key[i]]: 
                for k in pos_map[key[i - 1]]: 
                    distance = min(abs(j - k), n - abs(j - k)) + 1 
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + distance)

        return min(dp[-1][j] for j in pos_map[key[-1]])