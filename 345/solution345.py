class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aioueAIOUE")
        new_vowels = [i for i in s if i in vowels]
        strin = []

        for i in s:
            if i in vowels:
                strin.append(new_vowels.pop())
            else:
                strin.append(i)

        return "".join(strin)