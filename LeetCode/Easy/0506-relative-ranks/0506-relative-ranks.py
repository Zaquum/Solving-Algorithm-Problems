import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # sorting
        n = len(score)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        sorted_score = sorted(score, reverse = True)
        rank = dict()
        for i in range(n):
            if i < 3:
                rank[sorted_score[i]] = medals[i]
            else:
                rank[sorted_score[i]] = str(i+1)
        for i in range(n):
            score[i] = rank[score[i]]
        return score
    
        # heap
#         n = len(score)
        
#         heap = []
#         for i, s in enumerate(score):
#             heapq.heappush(heap, (-s, i))
        
#         i = 0
#         while heap:
#             _, idx = heapq.heappop(heap)
            
#             if i == 0:
#                 score[idx] = "Gold Medal"
#             elif i == 1:
#                 score[idx] = "Silver Medal"
#             elif i == 2:
#                 score[idx] = "Bronze Medal"
#             else:
#                 score[idx] = str(i+1)
            
#             i += 1
                
#         return score
        