class Solution {
    public int solution(int a, int b, int n) {
        /*
        n을 a로 나눈 몫: -> 돌려받을 콜라
        n을 a로 나눈 나머지: -> 남은 콜라
        돌려받을 콜라 + 남은 콜라로 n 갱신
        n이 a보다 작으면 끝
        */
        int result = 0;
        while(n >= a){
            int payback = (n / a) * b;
            result += payback;
            int remain = n % a;
            n = payback + remain;
        }
        return result;
    }
}