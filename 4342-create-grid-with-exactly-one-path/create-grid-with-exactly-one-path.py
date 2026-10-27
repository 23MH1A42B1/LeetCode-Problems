class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            row = ""
            for j in range(n):
                if i == 0 or j == n - 1:
                    row += "."
                else:
                    row += "#"
            grid.append(row)
        return grid