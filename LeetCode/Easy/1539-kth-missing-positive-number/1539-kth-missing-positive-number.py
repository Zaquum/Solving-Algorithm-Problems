class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        integer = 0
        idx = 0
        missing_idx = 0
        while missing_idx < k:
            integer += 1
            if idx < len(arr) and arr[idx] == integer:
                idx += 1
                continue
            missing_idx += 1
        return integer