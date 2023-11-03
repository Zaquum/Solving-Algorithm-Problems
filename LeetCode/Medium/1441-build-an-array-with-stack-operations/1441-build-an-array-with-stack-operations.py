class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        ans = []
        for i in range(1,n+1):
            s.append(i)
            last = len(s) - 1
            ans.append("Push")
            if target[last] != s[last]:
                ans.append("Pop")
                s.pop()
            if target == s:
                return ans
                