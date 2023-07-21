class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n # legnth of lengest ending in nums[i]
        count = [1] * n

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if length[i] >= length[j]:
                        length[j] = length[i] + 1
                        count[j] = count[i]
                    elif length[i] + 1 == length[j]:
                        count[j] += count[i]
        longest = max(length)
        return sum(c for l,c in zip(length, count) if l == longest)
                
        # DFS Time limit
        # max_len = [0]
        # ans = [0]
        # n = len(nums)
        # substr = [-1000000]
        # lengths = [0] * n
    
        # def dfs(idx, substr, length):
        #     if idx == n:
        #         if length == max_len[0]:
        #             ans[0] += 1
        #         elif length > max_len[0]:
        #             max_len[0] = length
        #             ans[0] = 1
        #         return

        #     if substr[-1] < nums[idx]:
        #         dfs(idx+1, substr + [nums[idx]], length + 1)
        #     dfs(idx+1, substr, length)

        # dfs(0, substr, 0)
        # return ans[0]