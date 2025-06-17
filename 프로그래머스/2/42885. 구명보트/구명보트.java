import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        /*
        가장 무게가 많은사람과 가장 적은 사람의 합이 제한 초과이면
        무게 많은사람은 혼자 타기
        이하이면 같이 타기
        i<j일 때 까지
        */
        int cnt=0;
        int i=0;
        int j=people.length-1;
        Arrays.sort(people);
        while(i<=j){
            int max = people[j];
            int min = people[i];
            if(max+min <= limit){
                i++;
                j--;
            }
            else{
                j--;
            }
            cnt++;
        }
        return cnt;
    }
}