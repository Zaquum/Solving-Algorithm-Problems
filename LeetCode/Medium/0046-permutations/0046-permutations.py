class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [] # answer
        def solve(array, remaining):
            if len(array) == n:
                ans.append(list(array))
                return
            for i in range(len(remaining)):
                solve(array + [remaining[i]], remaining[:i] + remaining[i+1:])
        solve([], nums)
        return ans