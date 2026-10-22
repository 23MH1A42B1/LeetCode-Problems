from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        ascending = all(
            nums[i] == (nums[0] + i) % n
            for i in range(n)
        )

        descending = all(
            nums[i] == (nums[0] - i) % n
            for i in range(n)
        )

        ans = float('inf')

        if ascending:
            k = (n - nums[0]) % n
            ans = min(ans, k, n - k + 2)

        if descending:
            k = (n - 1 - nums[0]) % n
            ans = min(ans, k + 1, n - k + 1)

        return ans if ans != float('inf') else -1
