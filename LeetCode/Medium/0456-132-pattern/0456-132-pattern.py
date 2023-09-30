class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if not nums or len(nums) < 3:
            return False

        stack = []
        thirdMax = float('-inf')
        
        # Traverse from right to left
        for num in reversed(nums):
            # If the current number is less than thirdMax, we've found a 132 pattern
            if num < thirdMax:
                return True
            # Pop numbers from the stack which are less than or equal to the current number
            while stack and stack[-1] < num:
                thirdMax = stack.pop()
            # Push the current number onto the stack
            stack.append(num)

        # If we've gone through the entire list without returning True, there's no 132 pattern
        return False