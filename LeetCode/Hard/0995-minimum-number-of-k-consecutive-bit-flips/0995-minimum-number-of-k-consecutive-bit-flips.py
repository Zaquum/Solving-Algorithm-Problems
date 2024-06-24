class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip = [0] * n
        flip_cnt = 0
        ans = 0

        for i in range(n):
            if i >= k:
                flip_cnt ^= flip[i - k]

            if nums[i] ^ flip_cnt == 0:
                if i + k > n:
                    return -1
                flip_cnt ^= 1
                flip[i] = 1
                ans += 1

        return ans