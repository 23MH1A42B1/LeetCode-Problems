
class Solution:
    def minOperations(self, s: str) -> int:
        if s == ''.join(sorted(s)):
            return 0

        n = len(s)

        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        if s[0] == mn or s[-1] == mx:
            return 1

        if s[0] == mx and s[-1] == mn:
            if s.count(mx) == n or s.count(mn) == n:
                return 1
            if s[1:-1].count(mx) > 0 or s[1:-1].count(mn) > 0:
                return 2
            return 3

        return 2
