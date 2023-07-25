class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def find_max(start, end):
            mid = (start + end)//2
            if start < end:
                if arr[mid] > arr[mid+1]:
                    return find_max(start, mid)
                else:
                    return find_max(mid+1, end)
            else:
                return start
        return find_max(0, len(arr)-1)