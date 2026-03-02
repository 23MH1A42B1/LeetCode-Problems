class Solution {
    public boolean hasAlternatingBits(int n) {
        
        int prev = -1;
        
        while(n > 0)
        {
            int bit = n % 2;
            
            if(bit == prev)
                return false;
                
            prev = bit;
            n = n / 2;
        }
        
        return true;
    }
}