class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_fold = s[1:]+s[:-1]
        return s in s_fold