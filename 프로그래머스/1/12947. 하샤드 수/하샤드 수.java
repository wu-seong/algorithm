class Solution {
    public boolean solution(int x) {
        int[] chars = String.valueOf(x).chars().map(c -> Character.getNumericValue(c)).toArray();
        int sum = 0;
        for(int num: chars){
            System.out.println(num);   
            sum += num;
        }
        return x % sum == 0;
    }
}