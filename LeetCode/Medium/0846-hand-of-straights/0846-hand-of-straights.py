class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        
        hand.sort()
        while hand:
            tmp = []
            flag = False
            while len(tmp) < groupSize and hand:
                cur = hand[0]
                if not tmp:
                    cur = hand.pop(0)
                    tmp.append(cur)
                if tmp and tmp[-1] + 1 not in hand:
                    flag = True
                    return
                elif tmp and tmp[-1] + 1 in hand:
                    idx = 0
                    for i in range(len(hand)):
                        if hand[i] == tmp[-1] + 1:
                            idx = i
                            break
                    cur = hand.pop(i)
                    tmp.append(cur)
            if flag:
                return False
            if len(tmp) != groupSize:
                return False
        return True
                