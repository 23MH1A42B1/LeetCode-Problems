class Solution {
    public int minOperations(String s) {
        
        int change1 = 0;
        int change2 = 0;
        
        for(int i = 0; i < s.length(); i++){
            
            char c = s.charAt(i);
            
            if(i % 2 == 0){
                if(c != '0') change1++;
                if(c != '1') change2++;
            }
            else{
                if(c != '1') change1++;
                if(c != '0') change2++;
            }
        }
        
        return Math.min(change1, change2);
    }
}