class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            check = stones[0] - stones[1]
            stones.pop(0)
            stones.pop(0)
            stones.append(check)

        return stones[0]