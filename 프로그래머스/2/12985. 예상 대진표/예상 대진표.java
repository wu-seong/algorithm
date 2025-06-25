class Solution
{
    public int solution(int n, int a, int b)
    {
        /*
        1: 2조, 4조
        2: 1조, 2조
        3: 1조
        (-1한 것에 2로 나눈 몫) 이 같으면 만남
        (-1한 것에 2로 나눈 몫) + 1
        */
        int round = 1;
        while(true){
            int groupA = ((a-1)/2) + 1;
            int groupB = ((b-1)/2) + 1;
            if(groupA == groupB){
                return round;
            }
            a = groupA;
            b = groupB;
            round++;
        }
    }
}