class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def possible(speed):
            time = sum(ceil(d/speed) for d in dist[:-1])
            time += dist[-1] / speed
            if time > hour:
                return False
            return time

        if len(dist) - 1 >= hour:
            return -1
        
        left,right = 1, 10**7
        while left < right:
            mid = (left+right) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left

        # O(n)
        # if len(dist) - 1 >= hour:
        #     return -1
        
        # speed = math.ceil(sum(dist) / hour) # Start from this speed

        # while True:
        #     total = 0.0
        #     for i in range(len(dist)):
        #         spend = dist[i] / speed
        #         if i != len(dist) - 1:  # if not the last train, round up to nearest hour
        #             spend = math.ceil(spend)
        #         total += spend
        #     if total <= hour:  # If we can reach in time, return speed
        #         return speed if speed <= 10**7 else -1
        #     speed += 1  # else, increase the speed