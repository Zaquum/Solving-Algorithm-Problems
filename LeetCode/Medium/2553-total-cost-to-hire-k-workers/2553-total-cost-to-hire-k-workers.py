class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        start = 0
        end = len(costs) - 1
        min_left = [] # left min heap
        min_right = [] # right min heap

        for _ in range(k):
            # left side
            while len(min_left) < candidates and start <= end:
                heapq.heappush(min_left, costs[start])
                start += 1
            # right side
            while len(min_right) < candidates and start <= end:
                heapq.heappush(min_right, costs[end])
                end -= 1
            # left가 비었다면
            if not min_left:
                ans += heapq.heappop(min_right)
            # right가 비었다면
            elif not min_right:
                ans += heapq.heappop(min_left)
            # left가 작으면
            elif min_left[0] <= min_right[0]:
                ans += heapq.heappop(min_left)
            # right가 작으면
            else:
                ans += heapq.heappop(min_right)
        return ans
        
        # @functools.lru_cache(None)
        # def solve(remain: Tuple[int], need_people:int):
        #     remain = list(remain)
        #     if need_people == 0:
        #         return 0
        #     if len(remain) < candidates:
        #         min_idx = remain.index(min(remain))
        #         min_cost = remain.pop(min_idx)
        #         return min_cost + solve(tuple(remain), need_people-1)
        #     else:
        #         first_candidates = remain[:candidates]
        #         last_candidates = remain[-candidates:]
        #         min_cost_first = min(first_candidates)
        #         min_cost_last = min(last_candidates)
        #         min_idx_first = first_candidates.index(min_cost_first)
        #         min_idx_last = len(remain) - candidates + last_candidates.index(min_cost_last)
        #         if min_cost_first < min_cost_last or (min_cost_first == min_cost_last and min_idx_first <= min_idx_last):
        #             remain.pop(min_idx_first)
        #             return min_cost_first + solve(tuple(remain), need_people - 1)
        #         else:
        #             remain.pop(min_idx_last)
        #             return min_cost_last + solve(tuple(remain), need_people - 1)
                
        # return solve(tuple(costs), k)