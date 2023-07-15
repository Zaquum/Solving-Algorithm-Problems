class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # 참석 + 바로 뒤거
        # 참석 x + 바로 뒤거
        n = len(events)
        events.sort()

        @functools.lru_cache(None)
        def dp(pre_end, ev_idx, k):
            
            if  k == 0 or ev_idx == n:
                return 0
            
            event = events[ev_idx]
            start, end, value = event

            # 날짜가 안맞으면 무조건 참석x + 바로 뒤거
            if start <= pre_end:
                return dp(pre_end, ev_idx + 1, k)
            
            return max(
                value + dp(end, ev_idx + 1, k - 1), # 참석 + 다음 것
                dp(pre_end, ev_idx + 1, k) # 참석x + 다음 것
            )

        return dp(0, 0, k)