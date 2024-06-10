class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h = sorted(heights)
        ans = 0
        for sorted_e, e in zip(sorted_h, heights):
            if sorted_e != e:
                ans += 1
        return ans