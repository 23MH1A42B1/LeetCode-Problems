class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        ans = ""
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = i + 1

                while s[j] != ')':
                    j += 1

                key = s[i + 1:j]

                if key in d:
                    ans += d[key]
                else:
                    ans += '?'

                i = j + 1
            else:
                ans += s[i]
                i += 1

        return ans