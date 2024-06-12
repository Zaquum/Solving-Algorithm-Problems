class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnts = defaultdict(int)
        for num in nums:
            cnts[num] += 1
        # print(cnts)
        idx = 0
        for i in range(3):
            nums[idx:idx+cnts[i]] = [i] * cnts[i]
            idx += cnts[i]
        return