class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        
        def dp(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            
            if start == end:
                return nums[start]
            
            memo[(start, end)] = max(nums[start] - dp(start + 1, end), nums[end] - dp(start, end - 1))
            
            return memo[(start, end)]
        
        return dp(0, n-1) >= 0
        # n = len(nums)
        # player_sum = 0
        # def solve(nums: List[int], start, end, player_sum, turn):
        #     if start > end:
        #         if player_sum >= 0:
        #             return True
        #         else:
        #             return False

        #     first = nums[start]
        #     last = nums[end]
        #     # player1 turn
        #     if turn == 0:
        #         return (solve(nums, start+1, end, player_sum + first, 1) or
        #                 solve(nums, start, end-1, player_sum + last, 1))
        #     # player2 turn
        #     elif turn == 1:
        #         return (solve(nums, start+1, end, player_sum - first, 0) and
        #                 solve(nums, start, end-1, player_sum - last, 0))

        # return solve(nums, 0, n-1, 0, 0)