class Solution {
    public int[] solution(long n) {
        
        String num = Long.toString(n);
        num = new StringBuilder(num).reverse().toString();
        String[] digit = num.split("");
        int[] result = new int[num.length()];
        for(int i=0; i<digit.length; i++){
            result[i] = Integer.parseInt(digit[i]);
            //System.out.println(d);    
        }
        
        return result;
    }
}