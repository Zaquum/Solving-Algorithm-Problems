class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height = [(height, name) for height, name in zip(heights, names)]
        name_height = sorted(name_height, key=lambda x: x[0], reverse=True)
        return [name for _, name in name_height]