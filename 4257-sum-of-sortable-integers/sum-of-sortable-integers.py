from collections import Counter
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                sorted_block = target[start:start + k]
                if Counter(block) != Counter(sorted_block):
                    valid = False
                    break
                descents = 0
                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        descents += 1

                if descents > 1:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
