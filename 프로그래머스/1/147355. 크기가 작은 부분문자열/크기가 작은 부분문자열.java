class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int solution(String t, String p) {
        /*
        1. p문자열 길이만큼 쪼개서 숫자 만들기
        2. 숫자와 p <= 비교해서 카운팅하기
        i+p.length <= t.length 일 때 까지 반복
        */
        int result=0;
        int length = p.length();
        long numP = Long.parseLong(p);
        for(int i=0; i+length <= t.length(); i++){
            long num = Long.parseLong(t.substring(i,i+length));
            log(num);
            if(num <= numP){
                result++;
            }
        }
        return result;
    }
}