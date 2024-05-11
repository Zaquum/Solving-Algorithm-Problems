from itertools import permutations
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted((w/q, q, w) for q, w in zip(quality, wage))
        
        max_heap = []
        sum_quality = 0
        min_cost = float('inf')
        
        for ratio, q, w in workers:
            heapq.heappush(max_heap, -q) # -10
            sum_quality += q # 10
        
            if len(max_heap) > k: 
                sum_quality += heapq.heappop(max_heap)
            
            if len(max_heap) == k:
                min_cost = min(min_cost, sum_quality * ratio)
                
        return min_cost