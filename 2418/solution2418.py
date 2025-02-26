class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        a = list(zip(names, heights))
        l1 = list(sorted(a, key=lambda x: x[1], reverse=True))
        l2 = list(map(lambda x: x[0], l1))
        return l2