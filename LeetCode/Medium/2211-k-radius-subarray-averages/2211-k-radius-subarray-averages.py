class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = []
        sub_sum = 0
        sub_avg = 0
        length = 2*k+1
        for idx, num in enumerate(nums):
            if idx - k < 0 or idx + k >= len(nums):
                avgs.append(-1)
                sub_sum += num
                continue
            elif idx == k:
                sub_sum += sum(nums[idx:idx+k+1])
                sub_avg = sub_sum // length
                avgs.append(sub_avg)
                continue
            sub_sum = sub_sum + nums[idx + k] - nums[idx - k - 1]
            sub_avg = sub_sum // length
            avgs.append(sub_avg)
        return avgs