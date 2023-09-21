class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        nums = sorted(nums1+nums2)
        print(nums)
        if (m+n)%2:
            return nums[(m+n)//2]
        else:
            # print(nums[(m+n)//2-1], nums[(m+n)//2])
            return (nums[(m+n)//2-1]+nums[(m+n)//2])/2