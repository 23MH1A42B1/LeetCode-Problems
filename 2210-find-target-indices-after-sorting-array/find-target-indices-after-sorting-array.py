class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        lst=[]
        for i in range(len(nums)):
            if nums[i]==target:
                lst.append(i)
        return lst