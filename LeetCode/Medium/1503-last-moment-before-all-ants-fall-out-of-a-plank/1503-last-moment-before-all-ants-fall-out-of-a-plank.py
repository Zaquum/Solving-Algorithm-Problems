class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left_times = [pos for pos in left]
        right_times = [n - pos for pos in right]
        return max(left_times + right_times)