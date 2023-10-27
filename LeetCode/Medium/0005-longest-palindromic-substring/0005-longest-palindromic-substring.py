class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        ans = ''
        for i in range(n):
            dp[i][i] = True
        ans = s[-1]

        maxLen = 1
        for lo in range(n-1, -1, -1):
            for hi in range(lo+1, n):
                if s[lo] == s[hi]:
                    if hi - lo == 1 or dp[lo+1][hi-1]:
                        dp[lo][hi] = True
                        # print(lo, hi)
                        if maxLen < hi - lo + 1:
                            maxLen = hi - lo + 1
                            ans = s[lo : hi+1]
        return ans