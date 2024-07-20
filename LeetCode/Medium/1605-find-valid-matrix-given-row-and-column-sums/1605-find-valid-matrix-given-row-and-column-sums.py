class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)] 

        for i in range(m):
            for j in range(n):
                min_value = min(rowSum[i], colSum[j]) 
                matrix[i][j] = min_value
                rowSum[i] -= min_value 
                colSum[j] -= min_value 

        return matrix