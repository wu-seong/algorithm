class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int rowLength = arr1.length;
        int colLength = arr1[0].length;
        int[][] sum = new int[rowLength][colLength];
        for(int i=0; i<rowLength; i++){
            for(int j=0; j<colLength; j++){
                sum[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        return sum;
    }
}