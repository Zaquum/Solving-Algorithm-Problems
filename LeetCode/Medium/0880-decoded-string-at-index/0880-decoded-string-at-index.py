class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
        for ch in reversed(s):
            k %= size
            if k == 0 and ch.isalpha():
                return ch
            
            if ch.isdigit():
                size /= int(ch)
            else:
                size -= 1