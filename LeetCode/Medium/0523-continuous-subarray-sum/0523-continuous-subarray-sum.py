class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix_sum = 0
        seen = {0: -1}
        
        for i in range(n):
            prefix_sum += nums[i]
            prefix_sum %= k     
            if prefix_sum in seen:
                if i - seen[prefix_sum] > 1: # check the length is more than 2
                    return True
            else:
                seen[prefix_sum] = i
        
        return False
    
        # O(n)