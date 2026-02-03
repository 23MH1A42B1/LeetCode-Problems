class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i < n - 2 and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False
        peak = i
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1
        if i == peak or i == n - 1:
            return False
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        return i == n - 1
