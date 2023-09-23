class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)

        dp = {}
        
        max_length = 0
        
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                # print(prev)
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            max_length = max(max_length, dp[word])
        # print(dp)
        return max_length