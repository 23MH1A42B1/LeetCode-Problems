class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        total = 0
        count = 0

        for x in nums:
            total += x

            if total - k in d:
                count += d[total - k]

            d[total] = d.get(total, 0) + 1

        return count