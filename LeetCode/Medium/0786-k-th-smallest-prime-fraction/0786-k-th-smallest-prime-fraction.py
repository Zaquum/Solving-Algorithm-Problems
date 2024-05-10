class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
        heapq.heapify(heap)
        for i in range(n):
            for j in range(i+1, n):
                heapq.heappush(heap, (arr[i] / arr[j], arr[i], arr[j]))
        ans = None
        while k:
            _, i, j = heapq.heappop(heap)
            ans = [i, j]
            k -= 1
        return ans