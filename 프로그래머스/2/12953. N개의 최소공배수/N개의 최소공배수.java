import java.util.*;

class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public static int gcd(int a, int b){
        // (a > b) a % b이면 b가 최대 공약수 
        if (a<b){
            int temp = a;
            a = b;
            b = temp;
        }
        while(true){
            if(a % b == 0){
                return b;
            }
            int temp = b;
            b = a % b;
            a = temp;
        }
    }
    public int solution(int[] arr) {
        /*
        두 수의 최대 공배수 = A * B / 최대 공약수
        최대 공약수 = GCD(A, B)
        한 쌍의 최대 공약수를 구하고
        해당 수를 넣음
        */
        
        if(arr.length == 1){
            return arr[0];
        }
        int result = 1;
        int n = arr.length;
        for(int i=0; i<n; i++){
            result = (result * arr[i]) / gcd(result, arr[i]);
            //log(result);
        }
        
        return result;
    }
}