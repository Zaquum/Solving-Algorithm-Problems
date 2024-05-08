class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = []
        for ch in s:
            if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9':
                if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
                    ch = ch.lower()
                words.append(ch)
        for i in range(len(words)):
            if words[i] != words[-(i+1)]:
                return False
        return True
        