class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(len(ranges)):
            start, end = max(0, i-ranges[i]), min(n, i+ranges[i])
            for j in range(start+1, end+1):
                dp[j] = min(dp[j], dp[start]+1)

        return dp[-1] if dp[-1] != float('inf') else -1