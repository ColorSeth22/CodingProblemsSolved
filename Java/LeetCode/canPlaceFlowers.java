class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
         int count = 0;
        if(flowerbed.length == 1){
            if(n == 0){
                return true;
            }
            return flowerbed[0] == 0;
        }
        for(int i = 0; i < flowerbed.length; i++){
            if(i == flowerbed.length - 1){
                if(flowerbed[i - 1] == 0 && flowerbed[i] == 0){
                    flowerbed[i] = 1;
                    count++;
                }
            }
            else if(i == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0) {
                flowerbed[i] = 1;
                count++;
            }
            else if(i > 0 && flowerbed[i] == 0 && flowerbed[i-1] == 0 && flowerbed[i + 1] == 0) {
                flowerbed[i] = 1;
                count++;
            }
        }
        return count >= n;
    }
}