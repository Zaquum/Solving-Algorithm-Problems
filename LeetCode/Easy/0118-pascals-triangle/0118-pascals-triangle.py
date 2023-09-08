class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([1])
        for i in range(numRows - 1):
            newRow = [1]
            for j in range(i):
                newRow.append(result[i][j]+result[i][j+1])
            newRow.append(1)
            result.append(newRow)
        return result
            