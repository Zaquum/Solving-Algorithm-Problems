class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp, heap = [0] * n, []
        for i in range(n):
            while heap and heap[0][1] < i - k:
                heapq.heappop(heap)
            
            dp[i] = nums[i]
            if heap:
                dp[i] = max(dp[i], -heap[0][0] + nums[i]) 
            
            if dp[i] > 0:
                heapq.heappush(heap, (-dp[i], i))
        
        # print(dp)
        return max(dp)