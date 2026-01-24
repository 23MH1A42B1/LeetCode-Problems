class Solution {
    public int findKOr(int[] nums, int k) {
        int result = 0;
        for (int bit = 0; bit < 31; bit++) {
            int count = 0;
            for (int num : nums) {
                if (((num >> bit) & 1) == 1) {
                    count++;
                }
            }
            if (count >= k) {
                result |= (1 << bit);
            }
        }

        return result;
    }
}
