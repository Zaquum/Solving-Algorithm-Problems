class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 110 001 010 100 -> 0 0 
        # 010 001 011 100 -> 
        for num in nums:
            k ^= num
        ans = 0
        print(k)
        while k:
            if k & 1:
                ans += 1
            k = k>>1
        return ans