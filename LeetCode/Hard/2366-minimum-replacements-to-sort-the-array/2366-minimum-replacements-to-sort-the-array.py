class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0

        prev = nums[-1]

        for i in range(n-2, -1, -1):
            # print(i)
            if nums[i] > prev:
                tmp = ceil(nums[i]/prev)
                operations += tmp-1
                prev = nums[i]//tmp
                # print(i)
            else:
                prev = nums[i]
                # print(i)
        return operations