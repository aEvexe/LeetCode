class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        count = len(a[-1])
        return int(count)
