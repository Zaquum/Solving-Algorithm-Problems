class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        max = 0
        for i in gain:
            if sum + i >= max:
                max = sum + i
            sum += i
        return max