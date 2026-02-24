class Solution {

    public int countPrimeSetBits(int left, int right) {

        int count = 0;

        java.util.Set<Integer> primes =
            java.util.Set.of(2,3,5,7,11,13,17,19);

        for(int i = left; i <= right; i++) {

            int bits = Integer.bitCount(i);

            if(primes.contains(bits)) {
                count++;
            }
        }

        return count;
    }
}