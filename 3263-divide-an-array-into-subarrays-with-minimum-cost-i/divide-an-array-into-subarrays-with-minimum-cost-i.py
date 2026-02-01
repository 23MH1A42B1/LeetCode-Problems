class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_cost = nums[0]
        rest = sorted(nums[1:])
        return first_cost + rest[0] + rest[1]
