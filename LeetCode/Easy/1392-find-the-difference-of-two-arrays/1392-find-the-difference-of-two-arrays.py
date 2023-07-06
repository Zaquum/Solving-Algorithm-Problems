class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_ans1 = set(nums1)
        set_ans2 = set(nums2)
        ans1 = set_ans1 - set_ans2
        ans2 = set_ans2 - set_ans1
        ans = []
        ans.append(ans1)
        ans.append(ans2)
        return ans