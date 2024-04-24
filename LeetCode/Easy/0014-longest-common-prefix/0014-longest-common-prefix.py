class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return shortest[:i]
                    
        return shortest