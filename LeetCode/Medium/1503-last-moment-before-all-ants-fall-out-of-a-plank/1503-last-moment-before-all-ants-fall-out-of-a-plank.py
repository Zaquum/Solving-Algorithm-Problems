class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left_fall_times = [pos for pos in left]
        
        right_fall_times = [n - pos for pos in right]
        
        return max(left_fall_times + right_fall_times)