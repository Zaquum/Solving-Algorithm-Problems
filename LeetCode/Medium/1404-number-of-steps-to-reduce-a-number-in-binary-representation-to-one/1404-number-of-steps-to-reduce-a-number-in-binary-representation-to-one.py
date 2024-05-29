class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            if s[i] == '1':
                num += 2**(len(s) - 1 - i)
        # print(num)
        step = 0 
        while num > 1:
            step += 1
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
        return step
        