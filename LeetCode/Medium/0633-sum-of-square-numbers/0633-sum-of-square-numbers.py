class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r = 0, int(sqrt(c))
        
        while l <= r:
            curr_sum = l * l + r * r  
            if curr_sum == c:
                return True 
            elif curr_sum < c:
                l += 1  
            else:
                r -= 1      
        return False 