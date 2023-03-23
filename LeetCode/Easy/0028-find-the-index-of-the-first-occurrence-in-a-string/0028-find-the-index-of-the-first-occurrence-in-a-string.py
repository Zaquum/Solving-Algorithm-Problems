class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if len(needle) > len(haystack):
        #     return -1
        i = 0
        while i < len(haystack):
            j = 0
            while j < len(needle) and i+j < len(haystack):
                if haystack[i+j] == needle[j]:
                    j += 1
                else:
                    break
            if j == len(needle):
                return i
            i += 1
        if i == len(haystack):
            return -1