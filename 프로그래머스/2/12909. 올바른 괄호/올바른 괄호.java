import java.util.*;
class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack(); 
        /*
        여는 괄호가 나오면 stack에 Push
        닫는 괄호가 나오면 pop
        닫는 괄호가 나왔는데 stack이 empty이면 false
        마지막에 stack이 남아 있는채로 끝나도 false
        */
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) == ')'){
                if(stack.isEmpty()){
                    return false;
                }
                else{
                    stack.pop();
                }
            }
            else{
                stack.push('(');
            }
        }
        // 닫히지 않는 괄호가 있는 경우
        if(!stack.isEmpty()){
            return false;
        }
        return true;
    }
}