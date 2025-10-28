import java.util.*;

class Solution {
    
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int i=0;i<scoville.length;i++){
            pq.add(scoville[i]);
        }
        
        while(!pq.isEmpty()){
            int m1 = pq.poll();
            if (m1>=K){
                return answer;
            }
            if(!pq.isEmpty()){
                int m2 = pq.poll();
                pq.add(m1+m2*2);
                answer+=1;
            }
            else{
                return -1;
            }
        }
        return answer;
    
    }
}