class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        result = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(1 - image[i][n-j-1])
            result.append(tmp)
        return result