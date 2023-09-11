class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        # result에 하나씩 결과 입력
        #  gr[i] = 3
        #   
        # set_group = set(groupSizes)
        dict_group = {}
        for i, size in enumerate(groupSizes):
            if size not in dict_group:
                dict_group[size] = []
            dict_group[size].append(i)
            if len(dict_group[size])==size:
                result.append(dict_group[size])
                dict_group[size] = []
        return result