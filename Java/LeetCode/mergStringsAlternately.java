class Solution {
    public String mergeAlternately(String word1, String word2) {
        String NewString = "";
        if(word1.length() > word2.length()){
            for(int i = 0; i < word2.length(); i++){
                NewString += word1.substring(i, i+1) + word2.substring(i, i+1);
            }
             NewString += word1.substring(word2.length());
        }
        else{
            for(int i = 0; i < word1.length(); i++){
                NewString += word1.substring(i, i+1) + word2.substring(i, i+1);
            }
            NewString += word2.substring(word1.length());
        }
        return NewString;
    }
}