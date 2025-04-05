class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public String solution(String phone_number) {
        String back = phone_number.substring(phone_number.length() - 4);
        StringBuilder prefix = new StringBuilder("");
        for(int i = 0; i<phone_number.length()-4; i++){
            prefix.append("*");
        }
        log(back);
        return prefix.toString() + back;
    }
}