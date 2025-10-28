class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        answer=dfs(target,0,0,numbers);
        
        return answer;
    }
    
    int[] calc = new int[]{1,-1};
    public int dfs(int target, int now, int level, int[] numbers){

        if (level==numbers.length){
            return now == target ? 1:0;
        }
        int cnt=0;
        for (int i=0;i<2;i++){
            cnt+=dfs(target,now+calc[i]*numbers[level],level+1,numbers);
        }
        return cnt;
    }
}