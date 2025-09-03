class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int[] TestArray = candies;
        List<Boolean> AnswerArray = new ArrayList<Boolean>();
        for(int i = 0; i < candies.length; i++){
            TestArray[i] += extraCandies;
            boolean testCase = true;
            for(int x = 0; x < candies.length; x++){
                if (TestArray[i] < TestArray[x] && x != i) {
                    testCase = false;
                    break;
                }
            }
            AnswerArray.add(testCase);
            TestArray[i] -= extraCandies;
        }
        return AnswerArray;
    }
}