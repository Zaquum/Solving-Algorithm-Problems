class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        idx = 0
        while idx < len(asteroids) - 1:
            if asteroids[idx] > 0 and asteroids[idx + 1] < 0:  # asteroids collide
                if abs(asteroids[idx]) > abs(asteroids[idx + 1]):
                    asteroids.pop(idx + 1)
                elif abs(asteroids[idx]) < abs(asteroids[idx + 1]):
                    asteroids.pop(idx)
                    idx -= 1
                else:
                    asteroids.pop(idx + 1)
                    asteroids.pop(idx)
                idx = 0  # move back one index
            else:
                idx += 1  # move forward one index
        return asteroids