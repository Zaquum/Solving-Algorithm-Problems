class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        for i in range(k):
            heappush(heap, (-nums[i],i)) # 0 ~ k-1, first
        ans.append(-heap[0][0])
        for i in range(k, len(nums)):
            heappush(heap, (-nums[i],i))
            while heap and (i - heap[0][1]) >= k:
                heappop(heap)
            ans.append(-heap[0][0])
        return ans