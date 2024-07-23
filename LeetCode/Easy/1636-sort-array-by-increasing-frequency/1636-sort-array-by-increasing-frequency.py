class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        sorted_nums = sorted(nums, key=lambda x: (freqs[x], -x))
        
        return sorted_nums