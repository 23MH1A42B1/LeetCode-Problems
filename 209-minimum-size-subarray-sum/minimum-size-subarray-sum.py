class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        current_sum = 0
        ans = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                ans = min(ans, right - left + 1)

                current_sum -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans