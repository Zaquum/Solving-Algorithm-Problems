class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        result = [[0 for _ in range(n)] for _ in range(n)] 
        for i in range(n):
            for j in range(n):
                result[i][n-j-1] = 1 - image[i][j]
        return result