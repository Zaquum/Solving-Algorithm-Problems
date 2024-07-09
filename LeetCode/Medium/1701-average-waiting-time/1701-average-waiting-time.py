class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        actual_arr = 0
        total_wait = 0
        for arr, time in customers:
            actual_arr = max(actual_arr, arr) + time
            total_wait += actual_arr - arr
            
        return total_wait / len(customers)
        # return total_wait