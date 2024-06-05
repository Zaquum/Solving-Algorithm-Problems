class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def count(s:str):
            freq = [0] * 26
            for ch in s:
                freq[ord(ch)-ord('a')] += 1
            return freq
        def common(freq1, freq2):
            common_freq = [min(ch1, ch2) for ch1, ch2 in zip(freq1, freq2)]
            return common_freq
        ans = count(words[0])
        for i in range(1, len(words)):
            ans = common(ans, count(words[i]))
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * ans[i])
        return result