class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total=0
        req=max(nums)
        for i in range(len(nums)):
            total+=req-nums[i]
        return total
