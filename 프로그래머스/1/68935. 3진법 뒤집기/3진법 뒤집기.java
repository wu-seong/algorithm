class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    
    
    public int solution(int n) {
        /*
        3진법 변환 -> 반대 -> 10진법 변환
        */
        StringBuilder sb =  new StringBuilder();
        boolean first = true;
        while(n >= 3){
            int remains = n % 3;
            n = n / 3;
            if(remains == 0 && first){
                continue;
            }
            first = false;
            sb.append(remains);
        }
        sb.append(n);
        
        int result = 0;
        for(int i=0; i<sb.length(); i++){
            //log(sb.charAt(i) + " " + Math.pow(3, sb.length()-1-i));
            result += (sb.charAt(i) - '0') * Math.pow(3, sb.length()-1-i);
        }
        return result;
    }
}