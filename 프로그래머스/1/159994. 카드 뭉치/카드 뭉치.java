class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        /*
        다음 찾는 단어가 양쪽에 있는지 확인
        있으면 인덱스 갱신
        없으면 No 리턴
        다 돌면 Yes
        */
        
        int i = 0;
        int j = 0;
        int n = cards1.length;
        int m = cards2.length;
        for(String word: goal){
            //log(word +" " + cards1[i] + " " + cards2[j]);
            if(i < n && cards1[i].equals(word)){
                i++;
                continue;
            }
            if(j < m && cards2[j].equals(word)){
                j++;
                continue;
            }
            return "No";
        }
        return "Yes";
    }
}