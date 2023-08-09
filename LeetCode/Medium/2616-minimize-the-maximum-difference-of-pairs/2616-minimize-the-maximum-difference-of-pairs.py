class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        start, end = 0, nums[-1] - nums[0]
        n = len(nums)

        def possible(a:int) -> bool:
            cnt, i = 0, 0
            while i < n-1 and cnt < p:
                if nums[i+1] - nums[i] <= a:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        while start < end:
            mid = (start+end)//2
            if possible(mid):
                end = mid
            else:
                start = mid + 1
        return start