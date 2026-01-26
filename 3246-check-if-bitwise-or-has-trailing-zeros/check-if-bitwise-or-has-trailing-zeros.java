class Solution {
    public boolean hasTrailingZeros(int[] nums) {
        int evenCount = 0;

        for (int num : nums) {
            if ((num & 1) == 0) { 
                evenCount++;
                if (evenCount >= 2)
                    return true;
            }
        }

        return false;
    }
}
