class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        nums1.sort()
        nums2.sort()
        
        ans = []
        while idx1 < n1 and idx2 < n2:
            if nums1[idx1] < nums2[idx2]:
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
            else:
                ans.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
        return ans
                