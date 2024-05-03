class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        # print(v1)
        v2 = version2.split('.')
        n = max(len(v1), len(v2))
        for i in range(n):
            # compare each int
            if i < len(v1) and i < len(v2):
                if int(v1[i]) > int(v2[i]):
                    return 1
                elif int(v1[i]) < int(v2[i]):
                    return -1
            # empty case
            else:
                if i >= len(v1) and int(v2[i]) != 0:
                    return -1
                elif i >= len(v2) and int(v1[i]) != 0:
                    return 1
        return 0