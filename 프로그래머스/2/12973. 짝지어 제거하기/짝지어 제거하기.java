import java.util.*;
class Solution
{
    public int solution(String s)
    {   /*
        스택이 비거나 top과 다르면 stack에 넣는다.
        스택이 비지 않았고 top과 같으면 pop한다.
       
        문자열 순회한 뒤 비어있지 않으면 0 
        */
        Stack<Character> stack = new Stack();
        for(char ch: s.toCharArray()){
            if(!stack.isEmpty() && stack.peek() == ch){
                stack.pop();
            }
            else{
                stack.push(ch);
            }
        }
        if(!stack.isEmpty()){
            return 0;
        }
        return 1;
    }
}