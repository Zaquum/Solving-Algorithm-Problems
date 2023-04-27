class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 0 -> 0, 1~3 -> 1, 4~8 -> 2 / 9 -> 3
        # 9 -> 3 9 12 2 3 4 6 12
        if n == 0:
            return 0
        else:
            return int(sqrt(n))
