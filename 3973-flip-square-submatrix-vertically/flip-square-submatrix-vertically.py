from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        for i in range(k // 2): 
            top_row = x + i
            bottom_row = x + k - 1 - i
            for j in range(k):
                grid[top_row][y + j], grid[bottom_row][y + j] = grid[bottom_row][y + j], grid[top_row][y + j]
        return grid