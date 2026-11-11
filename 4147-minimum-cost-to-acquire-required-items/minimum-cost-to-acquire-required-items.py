class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        mn = min(need1, need2)
        mx = max(need1, need2)

        option1 = need1 * cost1 + need2 * cost2

        option2 = mn * costBoth + (need1 - mn) * cost1 + (need2 - mn) * cost2

        option3 = mx * costBoth

        return min(option1, option2, option3)