# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        lo, hi = 0, n - 1
        # find peak
        while lo < hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid        
        peak = lo
        # find target with binary search
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi)//2
            value = mountain_arr.get(mid)
            if value == target:
                return mid
            elif value < target:
                lo = mid + 1
            else:
                hi = mid - 1
        lo, hi = peak, n - 1
        while lo <= hi:
            mid = (lo + hi)//2
            value = mountain_arr.get(mid)
            if value == target:
                return mid
            elif value < target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1