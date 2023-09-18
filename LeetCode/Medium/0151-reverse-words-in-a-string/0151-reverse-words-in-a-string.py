class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0
        result = ""
        for i in range(n):
            if s[i] != ' ' and (i==0 or s[i-1] == ' '):
                start = i
            elif s[i] == ' ' and i > 0 and s[i-1] != ' ':
                end = i
                result = " " + s[start:end] + result
        if s[n-1] != ' ':
            result = s[start:] + result
        return result.strip()