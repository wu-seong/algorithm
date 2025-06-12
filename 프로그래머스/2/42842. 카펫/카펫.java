class Solution {
    public static void log(Object o){
        System.out.println(o);
    }
    public int[] solution(int brown, int yellow) {
        /*
        합의 제곱근까지 약수 구해서 
        가로 세로 가정해서 (가로-2) * (세로-2) = yellow인지 판단하기
        */
        int sum = brown + yellow;
        int root = (int)Math.sqrt(sum);
        
        //log(root);
        for(int height = 3; height <= root; height++){
            if(sum % height == 0){
                int width = sum / height;
                int expected = (height - 2) * (width - 2);
                if(expected == yellow){
                    return new int[]{width, height};
                }
            }
        }
        return new int[]{};
    }
}