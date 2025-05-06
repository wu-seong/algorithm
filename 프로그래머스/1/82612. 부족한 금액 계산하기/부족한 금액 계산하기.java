class Solution {
    public long solution(int price, int money, int count) {
        /*
        count 까지의 시그마 구하기
        s = count*(count + 1)/2
        total = s * price
        */
        long s = count*(count+1)/2;
        long need = s*price;
        return need <= money ? 0 : need - money; 
    }
}