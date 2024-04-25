class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = {}
        

        for ch in s:
            max_len = 0
            for diff in range(-k, k + 1):
                neighbor_char = chr(ord(ch) + diff)
                if neighbor_char in dp:
                    max_len = max(max_len, dp[neighbor_char])

            dp[ch] = max_len + 1
        # print(dp)
        return max(dp.values())