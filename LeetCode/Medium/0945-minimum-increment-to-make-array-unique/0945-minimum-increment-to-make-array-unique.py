class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # 1 1 2 2 3 7
        # 1 
        # 1 2 3 4 5 7
        # 1 1 3 4 5 6 
        nums.sort()
        curmax = 0
        ans = 0
        for num in nums:
            curmax = max(curmax, num)
            ans += curmax - num
            curmax += 1
        return ans
            
        