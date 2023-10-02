class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A_count = sum(1 for i in range(1, len(colors)-1) if colors[i-1:i+2] == "AAA") 
        B_count = sum(1 for i in range(1, len(colors)-1) if colors[i-1:i+2] == "BBB") 

        while A_count > 0 or B_count > 0:
            if A_count > 0: 
                A_count -= 1
            else:
                return False

            if B_count > 0: 
                B_count -= 1
            else:
                return True

        return False  # default case