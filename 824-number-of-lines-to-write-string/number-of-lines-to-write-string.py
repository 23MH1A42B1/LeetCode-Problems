class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        lines = 1
        current_width = 0

        for ch in s:
            w = widths[ord(ch) - ord('a')]

            if current_width + w > 100:
                lines += 1
                current_width = w
            else:
                current_width += w

        return [lines, current_width]
