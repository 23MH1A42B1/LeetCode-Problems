class Solution {
    public boolean areSimilar(int[][] mat, int k) {
        int m = mat.length;
        int n = mat[0].length;
        
        // Effective shift after k operations
        int shift = k % n;
        
        for (int i = 0; i < m; i++) {
            if (!isRowSame(mat[i], shift, i % 2 == 0)) {
                return false;
            }
        }
        return true;
    }
    
    private boolean isRowSame(int[] row, int shift, boolean evenRow) {
        int n = row.length;
        for (int j = 0; j < n; j++) {
            int newIndex;
            if (evenRow) {
                
                newIndex = (j + shift) % n;
            } else {
                
                newIndex = (j - shift + n) % n;
            }
            if (row[j] != row[newIndex]) {
                return false;
            }
        }
        return true;
    }
}