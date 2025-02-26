class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        b = sorted(a, key=lambda x: x[-1])
        c = list(map(lambda x: x[:-1], b))
        return" ".join(c)