class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = {}
        nums_set = set(nums)
        for num in nums_set:
            visited[num] = 0
        for num in nums:
            visited[num] += 1
        for k, v in visited.items():
            if v == 1:
                return k

        # return ans