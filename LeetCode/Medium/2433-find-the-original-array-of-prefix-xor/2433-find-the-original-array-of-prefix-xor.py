class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # 101 000 -> 101
        cur = 0
        ans = []
        for num in pref:
            elem = cur^num
            ans.append(elem)
            cur = cur^elem
        return ans
        