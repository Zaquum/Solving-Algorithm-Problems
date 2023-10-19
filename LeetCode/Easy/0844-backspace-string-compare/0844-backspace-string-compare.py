class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ = []
        t_ = []
        for i in range(len(s)):
            if s[i] == '#':
                if s_:
                    s_.pop()
            else:
                s_.append(s[i])

        for i in range(len(t)):
            if t[i] == '#':
                if t_:
                    t_.pop()
            else:
                t_.append(t[i])
        
        return s_ == t_