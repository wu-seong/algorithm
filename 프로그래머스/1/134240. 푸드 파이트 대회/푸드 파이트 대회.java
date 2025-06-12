class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public String solution(int[] food) {
        /*
        각 음식마다 2로 나눈 몫 만큼 문자열에 add한다 끝나면 0이랑 반대 붙이기
        */
        
        StringBuilder result = new StringBuilder();
        for(int i=1; i<food.length; i++){
            int cnt = food[i]/2;
            
            for(int j=0; j<cnt; j++){
                result.append(i);
            }
        }
        //log(result);
        result.append("0" + new StringBuilder(result).reverse());
        return result.toString();
    }
}