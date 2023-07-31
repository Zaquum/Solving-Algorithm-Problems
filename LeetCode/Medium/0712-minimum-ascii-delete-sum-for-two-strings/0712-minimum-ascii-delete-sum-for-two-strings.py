class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        def solve(s1, s2):
            n1, n2 = len(s1), len(s2)
            dp = [[0] * (n2+1) for _ in range(n1+1)]
            
            for i in range(n1):
                for j in range(n2):
                    if s1[i] == s2[j]:
                        dp[i+1][j+1] = dp[i][j] + ord(s1[i])
                    else:
                        dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
            return dp[-1][-1]

        common_letter = solve(s1,s2)
        total = 0
        for s in s1:
            total += ord(s)
        for s in s2:
            total += ord(s)
        return total - common_letter * 2