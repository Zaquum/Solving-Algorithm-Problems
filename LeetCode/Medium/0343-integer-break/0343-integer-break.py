class Solution:
    def integerBreak(self, n: int) -> int:
        # 1 = 1
        # 2 = 1
        # 3 = 1 2
        # 4 = 2 2
        # 5 = 2 3
        # 6 = 3 3
        # 7 = 2 2 3
        # 8 = 2 3 3
        # 9 = 3 3 3
        # 10 = 3 3 4
        # 11 = 3 4 4
        # 12 = 3 3 3 3
        # 13 = 3 3 3 4
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        count_3, r = 0, n
        while r > 3:
            r -= 3
            count_3 += 1
        
        if r == 0:
            return 3**count_3
        elif r == 1:
            return 3**(count_3-1) * 4
        elif r == 2:
            return 3**count_3 * 2
        elif r == 3:
            return 3**count_3 * 3        

        