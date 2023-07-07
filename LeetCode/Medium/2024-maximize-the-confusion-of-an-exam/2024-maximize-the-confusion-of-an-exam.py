class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def solve(c: str) -> int:
            ans = 0
            low = -1
            changed = 0
            for i in range(len(answerKey)):
                if answerKey[i] == c:
                    changed += 1
                while changed > k:
                    low += 1
                    if answerKey[low] == c:
                        changed -= 1
                ans = max(ans, i - low)
            return ans
        return max(solve('T'), solve('F'))