class Solution {
    public int evenNumberBitwiseORs(int[] nums) {
        int result = 0;

        for (int num : nums) {
            if ((num & 1) == 0) { 
                result |= num;
            }
        }

        return result;
    }
}
