class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prev_finish = -1
        total_wait = 0
        for arr, time in customers:
            # first case
            if prev_finish < 0:
                prev_finish = arr + time
                total_wait += time
                continue
            
            if prev_finish <= arr:
                prev_finish = arr + time
            else:
                total_wait += prev_finish - arr
                prev_finish += time
                
            total_wait += time
            
            print(prev_finish, total_wait)
        return total_wait / len(customers)
        # return total_wait