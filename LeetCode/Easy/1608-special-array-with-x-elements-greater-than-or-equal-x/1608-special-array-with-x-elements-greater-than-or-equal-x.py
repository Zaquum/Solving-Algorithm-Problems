class Solution:
    def specialArray(self, nums: List[int]) -> int:
        tmp = max(nums)
        for cur in range(tmp, -1, -1):
            cnt = 0
            for num in nums:
                if cur <= num:
                    cnt += 1
            # print(cur)
            if cnt == cur:
                return cur
        return -1