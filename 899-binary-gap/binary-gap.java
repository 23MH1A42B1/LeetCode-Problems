class Solution {
    public int binaryGap(int n) {
        
        int lastPosition = -1;
        int maxDistance = 0;
        int position = 0;
        
        while (n > 0) {
            
            if ((n & 1) == 1) {
                
                if (lastPosition != -1) {
                    int distance = position - lastPosition;
                    maxDistance = Math.max(maxDistance, distance);
                }
                
                lastPosition = position;
            }
            
            position++;
            n = n >> 1;
        }
        
        return maxDistance;
    }
}