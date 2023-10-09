class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarysearch(target):
            start, end = 0, len(nums)
            while start < end:
                mid = (start+end)//2
                if nums[mid] < target:
                    start = mid + 1
                else :
                    end = mid
            return start
        
        start = binarysearch(target)
        end = binarysearch(target+1)-1

        if start <= end:
            return [start, end]
        # print(start, end)
        return [-1,-1] 