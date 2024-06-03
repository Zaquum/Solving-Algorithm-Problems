class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        len_s = min(len(s), len(t))
        i_s, i_t = 0, 0
        while i_s < len(s) and i_t < len(t):
            if s[i_s] == t[i_t]:
                i_s += 1
                i_t += 1
            else:
                i_s += 1
        return len(t) - i_t