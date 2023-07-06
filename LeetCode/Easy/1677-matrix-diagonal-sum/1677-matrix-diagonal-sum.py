class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        start_idx = 0
        end_idx = len(mat) - 1
        ans = 0
        for nums in mat:
            ans += nums[start_idx]
            ans += nums[end_idx]
            start_idx += 1
            end_idx -= 1
        if len(mat)%2 == 1:
            center_idx = int((len(mat)-1)/2)
            ans -= mat[center_idx][center_idx]
        return ans