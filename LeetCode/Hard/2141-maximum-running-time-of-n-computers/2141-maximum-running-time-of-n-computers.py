class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, (sum(batteries) // n) + 1
        
        def possible(x):
            return sum(min(x, b) for b in batteries) >= n * x
        
        while left < right:
            mid = (left+right)//2
            if  possible(mid):
                left = mid+1
            else:
                right = mid
        return left if possible(left) else left - 1