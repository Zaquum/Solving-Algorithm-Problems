import heapq
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        ans = 0
        heapq.heapify(heap)
        for happy in happiness:
            heapq.heappush(heap, -happy)
        
        turn = 0
        while k > 0:
            tmp = heapq.heappop(heap)
            tmp = -tmp - turn
            
            if tmp <= 0:
                break
                
            ans += tmp
             
            # update
            turn += 1
            k-= 1
        
        return ans