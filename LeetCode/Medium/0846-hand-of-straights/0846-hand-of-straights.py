class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        
        # 딕셔너리를 순회하면서 그룹을 만들 수 있는지 확인
        while counter:
            # 가장 작은 카드 값부터 시작하여 그룹 생성
            start = min(counter)
            for i in range(start, start + groupSize):
                # 만약 현재 카드 값이 딕셔너리에 없거나, 해당 카드 값의 개수가 0 이하라면 False 반환
                if i not in counter or counter[i] <= 0:
                    return False
                # 그룹에서 해당 카드 값을 하나 뺍니다.
                counter[i] -= 1
                # 만약 그룹에서 해당 카드 값을 모두 사용했다면 딕셔너리에서 제거합니다.
                if counter[i] == 0:
                    del counter[i]
        # 모든 그룹을 만들었으므로 True 반환
        return True
                