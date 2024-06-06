class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        
        def grouping(start):
            next_val = hand[start] + 1
            hand[start] = -1
            cnt = 1
            start += 1
            while start < n and cnt < groupSize:
                if hand[start] == next_val:
                    hand[start] = -1
                    next_val += 1
                    cnt += 1
                start += 1
            return cnt == groupSize
        
        hand.sort()
        for i in range(n):
            if hand[i] >= 0:
                if not grouping(i):
                    return False
        return True
 