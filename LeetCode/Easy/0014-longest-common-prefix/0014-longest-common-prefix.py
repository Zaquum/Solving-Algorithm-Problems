class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret=""
        # if not strs:
        #     return ret
        minStr=min(strs,key=len)
        for i in range(len(minStr)):
            cur=strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != cur:
                    return ret
            ret=ret+cur
        return ret