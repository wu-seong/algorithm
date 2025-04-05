class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public String solution(String s) {
        if(s.length() % 2 == 0){
            char[] chars = new char[]{
                (s.charAt((int)s.length()/2 - 1)),
                (s.charAt((int)s.length()/2))
            };
            return new String(chars);
        }
        else{
            char[] chars = new char[]{
                s.charAt((int)s.length()/2)
                };
            return new String(chars);
        }
    }
}