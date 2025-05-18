import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        /*
        
        */
        int[] result = new int[commands.length];
        for(int i=0; i<commands.length;i++){
            int s = commands[i][0]-1, e = commands[i][1], k = commands[i][2]-1;
            int[] newArray = Arrays.copyOfRange(array, s, e);
            Arrays.sort(newArray);
            // for(int num: newArray){
            //     System.out.print(num);
            // }
            // System.out.println();
            result[i] = newArray[k];
        }
        // for(int num: result){
        //     System.out.println(num);
        // }
        return result;
    }
}