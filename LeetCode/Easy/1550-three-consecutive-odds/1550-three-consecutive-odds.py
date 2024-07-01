class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        q = deque()
        if len(arr) < 3:
            return False
        
        for i in range(2):
            cur = True if arr[i] % 2 != 0 else False
            q.append(cur)
        for i in range(2, len(arr)):
            cur = True if arr[i] % 2 != 0 else False
            # print(cur)
            q.append(cur)
            if all(q):
                return True
            q.popleft()
        return False