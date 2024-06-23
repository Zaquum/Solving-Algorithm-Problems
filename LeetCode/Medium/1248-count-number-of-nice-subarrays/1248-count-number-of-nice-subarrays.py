class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnts = [0] * (n + 1)
        cnts[0] = 1
        ans = 0
        tmp = 0
        for num in nums:
            tmp += num & 1
            if tmp - k >= 0:
                ans += cnts[tmp - k]
            cnts[tmp] += 1
        print(cnts)
        return ans