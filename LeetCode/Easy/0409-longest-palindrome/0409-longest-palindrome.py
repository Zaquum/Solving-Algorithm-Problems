class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnts = defaultdict(int)
        for ch in s:
            cnts[ch] += 1
        ans = 0
        odd = False
        for ch, cnt in cnts.items():
            ans += cnt // 2 * 2
            if cnt % 2 == 1 and not odd:
                odd = True
                ans += 1
        return ans