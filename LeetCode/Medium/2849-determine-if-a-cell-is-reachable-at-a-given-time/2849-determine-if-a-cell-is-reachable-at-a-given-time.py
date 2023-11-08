class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dist_x = abs(sx - fx)
        dist_y = abs(sy - fy)
        dist_min = min(dist_x, dist_y) + abs(dist_x - dist_y)
        if dist_min == 0:
            if t == 1:
                return False
            else:
                return True
        return t >= dist_min