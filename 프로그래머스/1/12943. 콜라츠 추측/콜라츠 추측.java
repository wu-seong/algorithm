class Solution{
    public static void log(Object o){
        System.out.println(o);
    }
    public long collatz(long num){
        if(num % 2 == 0){
            return num/2;
        }
        else{
            return (num*3) + 1;
        }
    }
    public int solution(long num) {
        int cnt = 0;
        while(true){
            //log(num);
            // check
            if(num == 1){
                return cnt;
            }
            // before
            if(cnt == 500){
                return -1;
            }
            //collatz 
            num = collatz(num);
            cnt += 1;
        }
    }
}