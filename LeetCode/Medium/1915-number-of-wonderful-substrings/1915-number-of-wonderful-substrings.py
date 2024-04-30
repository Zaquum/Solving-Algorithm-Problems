class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask_count = defaultdict(int)
        mask_count[0] = 1

        mask = 0
        ans = 0
        for ch in word:
            mask ^= (1 << (ord(ch) - ord('a')))

            ans += mask_count[mask]
            for i in range(10):
                ans += mask_count[mask ^ (1 << i)]

            mask_count[mask] += 1

        return ans