class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi=float('-inf')
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            if sum>maxi:
                maxi=sum
            if sum<0:
                sum=0
        return maxi