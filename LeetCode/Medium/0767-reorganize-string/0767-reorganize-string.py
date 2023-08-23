class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char,0) + 1
        
        max_heap = []
        for char, cnt in freq.items():
            heapq.heappush(max_heap, (-cnt, char))
        
        if -max_heap[0][0] > (len(s)+1)/2:
            return ""

        ans = []
        prev_cnt, prev_char = 0, ''

        while max_heap:
            cnt, char = heapq.heappop(max_heap)
            ans.append(char)
            if prev_cnt < 0:
                heapq.heappush(max_heap, (prev_cnt, prev_char))
            
            prev_cnt, prev_char = cnt + 1, char
        return "".join(ans)