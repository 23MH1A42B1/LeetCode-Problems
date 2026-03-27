class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        effective_k = k % n
        
        if effective_k == 0:
            return True
            
        for row in mat:
            for j in range(n):
                if row[j] != row[(j + effective_k) % n]:
                    return False
        return True