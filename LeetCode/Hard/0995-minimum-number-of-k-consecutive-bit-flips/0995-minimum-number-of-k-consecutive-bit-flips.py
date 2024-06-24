class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip = [0] * n
        is_flip = 0
        ans = 0

        for i in range(n):
            if i >= k:
                is_flip ^= flip[i - k]

            if nums[i] ^ is_flip == 0:
                if i + k > n:
                    return -1
                is_flip ^= 1
                flip[i] = 1
                ans += 1

        return ans