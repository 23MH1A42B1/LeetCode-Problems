class Solution {
    public String reverseWords(String s) {

        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            StringBuilder sb = new StringBuilder(word);
            sb.reverse();
            result.append(sb).append(" ");
        }
        return result.toString().trim();
    }
}
