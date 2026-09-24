class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit_sum = sum(int(x) for x in str(nums[i]))

            if digit_sum == i:
                return i
                break
        else:
            return -1