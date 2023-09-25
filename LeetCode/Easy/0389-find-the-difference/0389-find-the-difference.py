class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_ = sorted(s)
        t_ = sorted(t)
        for i in range(len(s_)):
            if s_[i] != t_[i]:
                return t_[i]
        return t_[-1]