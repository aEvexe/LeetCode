class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [1] + digits

#2

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digit_st = "".join(map(str, digits))

        icrement_digit = int(digit_st) + 1

        st_digit = str(icrement_digit)

        new_digit = list(map(int, st_digit))

        return new_digit