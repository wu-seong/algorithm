import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        /*
        9 5 34 30 3
        내림차순인데
        303
        30
        
        어떤 수가 오름차순이면 해당 수를 먼저 위치
        
        32
        320
        
        322 32
        32 322
        
        344 34
        34 344
        
        30330
        30303
        앞에거랑 첫 자리를 먼저 비교
        첫자리가 더 작으면 그대로
        첫자리가 더 크면 바꾸기
        첫자리가 같으면
        그 다음 자릿수 비교
        그 다음 자릿수가 없으면
        추가적으로 있는 수와 앞 수를 비교
        
        정렬기준을 변경
        문자열로 변경하고
        각 자릿수를 앞에서 부터 비교
        내림차순이므로 b-a
        만약 둘의 자릿수가 다르다면
        짧은 것을 기준으로 비교
        
        만약 짧은 것을 기준으로 똑같다면,
        그 뒤에 덧붙여져 있는 것과 똑같은 부분을 비교
        
        덧붙여져 있는 수 > 똑같은 부분이면 긴 것을 반환
        */
        String[] numStrings = new String[numbers.length];
        for(int i=0; i<numbers.length; i++){
            numStrings[i] = Integer.toString(numbers[i]);
        }
            
        Arrays.sort(numStrings, (a,b) -> (b + a).compareTo(a + b));
        StringBuilder result = new StringBuilder("");
        boolean allZero = true;
        for(String s: numStrings){
            if(!s.equals("0")){
                allZero = false;
            }           
            
            if(!allZero){
                result.append(s);
            }
        }
        
        return allZero ? "0" : result.toString();
        
    }
}