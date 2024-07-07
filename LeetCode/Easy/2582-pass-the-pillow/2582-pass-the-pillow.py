class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur_time = 0
        cur_person = 1
        increase = 1
        while cur_time < time:
            if cur_person == n:
                increase = -1
            elif cur_person == 1:
                increase = 1
            cur_person += increase
            cur_time += 1
        return cur_person
            