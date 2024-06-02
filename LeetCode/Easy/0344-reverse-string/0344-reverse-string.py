class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            tmp = s[-(i+1)]
            # print(tmp)
            s[-(i+1)] = s[i]
            s[i] = tmp