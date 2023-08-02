class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # ans = [] # answer
        # def solve(array, remaining):
        #     if len(array) == n:
        #         ans.append(list(array))
        #         return
        #     for i in range(len(remaining)):
        #         solve(array + [remaining[i]], remaining[:i] + remaining[i+1:])
        # solve([], nums)
        # return ans

        n = len(nums)
        ans = [] # answer
        def solve(array, k):
            if k == n:
                ans.append(list(array))
                return
            for i in range(n):
                # array.append(nums[i])
                if nums[i] in array:
                    continue
                solve(array + [nums[i]], k+1)
                # array.remove(nums[i])
        solve([], 0)
        return ans