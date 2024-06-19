class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dif_profit = sorted(zip(difficulty, profit), key=lambda x: x[0])
        
        n = len(dif_profit)
        
        max_profit = [0] * n
        max_profit[0] = dif_profit[0][1]
        
        for i in range(1, n):
            max_profit[i] = max(max_profit[i-1], dif_profit[i][1])
        
        def find_job(worker):
            left, right = 0, n - 1
            if worker < dif_profit[0][0]:
                return 0
            
            while left <= right:
                mid = (left + right) // 2
                if dif_profit[mid][0] <= worker:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return max_profit[right]
        
        total_profit = 0
        for w in worker:
            total_profit += find_job(w)
        
        return total_profit