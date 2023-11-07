class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        times = []

        for i in range(n):
            time = (dist[i] + speed[i] - 1)//speed[i]
            times.append(time)

        times.sort()
        print(times)
        for i, t in enumerate(times):
            if t <= i:
                return i
        return len(times)

        # 4 2 3
        # 2 1 1