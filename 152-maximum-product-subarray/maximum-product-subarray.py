class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxi, mini = mini, maxi

            maxi = max(nums[i], maxi * nums[i])
            mini = min(nums[i], mini * nums[i])

            ans = max(ans, maxi)

        return ans