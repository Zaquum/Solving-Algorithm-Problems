class Solution:
    def minimumDeletions(self, s: str) -> int:
        # From GPT
        
        n = len(s)

        # Prefix counts
        a_count = [0] * (n + 1)
        b_count = [0] * (n + 1)

        for i in range(1, n + 1):
            a_count[i] = a_count[i - 1] + (1 if s[i - 1] == 'a' else 0)
            b_count[i] = b_count[i - 1] + (1 if s[i - 1] == 'b' else 0)

        # Suffix counts
        a_count_suffix = [0] * (n + 1)
        b_count_suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            a_count_suffix[i] = a_count_suffix[i + 1] + (1 if s[i] == 'a' else 0)
            b_count_suffix[i] = b_count_suffix[i + 1] + (1 if s[i] == 'b' else 0)

        # Find the minimum deletions required to make the string balanced
        min_deletions = float('inf')

        for i in range(n + 1):
            deletions = b_count[i] + a_count_suffix[i]
            min_deletions = min(min_deletions, deletions)

        return min_deletions        