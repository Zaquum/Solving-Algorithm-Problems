class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            value=int(str(x)[::-1])
        else:
            value=-int(str(-x)[::-1])
            
        if value not in range(-2**31,2**31):
            value=0;
            
            
        return value