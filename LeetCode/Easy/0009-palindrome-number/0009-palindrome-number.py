class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str=str(x)
        x_reverse=str(x)[::-1]
        if x_reverse==x_str:
            return True
        else:
            return False