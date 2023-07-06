class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -50000
        sell = 0
        
        # case1 : buy한 상태면 팔거나 그대로거나
        # case2 : sell한 상태면 그대로거나 사거나
        for price in prices:
            buy = max(buy, sell - price) # -1 -1 -1 -1 -1
            sell = max(sell, buy + price - fee) # 0 0 3 3
        
        return sell