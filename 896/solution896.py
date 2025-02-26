class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)