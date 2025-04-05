class Solution {
    public long solution(long n) {
        System.out.println((long)Math.sqrt(n) / 1 + "" + Math.sqrt(n));
        if((long)Math.sqrt(n) / 1 == Math.sqrt(n)){
            return (long)Math.pow((long)(Math.sqrt(n))+1,2);
        }
        return - 1;
    }
}