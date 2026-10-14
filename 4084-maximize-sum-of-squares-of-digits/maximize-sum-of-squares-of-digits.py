class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        k, remainder = divmod(sum, 9)

        ans = "9" * k

        if remainder > 0:
            ans += str(remainder)

        ans += "0" * (num - len(ans))

        return ans