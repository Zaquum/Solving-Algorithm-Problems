class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = 0
        dictionary = defaultdict(int)
        dictionary[0] = 1
        cnt = 0
        for i in range(n):
            prefix_sum += nums[i]
            prefix_sum %= k
            if prefix_sum in dictionary:
               cnt += dictionary[prefix_sum]
            dictionary[prefix_sum] += 1
        return cnt
            