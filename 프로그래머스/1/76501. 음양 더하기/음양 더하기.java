class Solution {
    public static void print(Object s){
        System.out.println(s);
    }
    public int calculate(int sum, int num, boolean sign){
        if(sign){
            return sum += num;
        }
        else{
            return sum -= num;
        }
    }
    public int solution(int[] absolutes, boolean[] signs) {
        int sum = 0;
        for(int i=0; i<absolutes.length; i++){
            sum = calculate(sum, absolutes[i], signs[i]);
        }
        print(sum);
        System.out.println(sum);
        return sum;
    }
}