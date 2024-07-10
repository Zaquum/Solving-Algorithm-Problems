class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log[:-1] == '..':
               ans = max(0, ans - 1)
            elif log[:-1] == '.':
                continue
            else:
                ans += 1
        return ans