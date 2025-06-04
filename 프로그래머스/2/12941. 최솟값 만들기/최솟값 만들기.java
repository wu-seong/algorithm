import java.util.*;
class Solution
{
    public int solution(int []A, int []B)
    {
        /*
        A는 오름차순 정렬, B는 내림차순 정렬해서 순서대로 곱해서 누적합
        */
        Arrays.sort(A);
        Arrays.sort(B);
        
        int sum = 0;
        for(int i=0; i<A.length; i++){
            sum += A[i] * B[A.length-1-i];
        }
        return sum;
    }
}