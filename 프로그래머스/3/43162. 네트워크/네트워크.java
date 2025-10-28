import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visited = new int[n];

        for (int i=0;i<n;i++){
            if (visited[i]==0){
                visited[i]=1;
                bfs(i,n,computers,visited);
                answer++;
            }
            
        }
        return answer;
    }
    
    private void bfs(int now, int n, int[][] computers, int[] visited){
        Queue<Integer> que = new LinkedList<>();
        que.add(now);
        while(!que.isEmpty()){
            int cur=que.poll();
            for (int next = 0; next < n; next++) {
                if (next == cur) continue; 
                if (computers[cur][next] == 1 && visited[next] == 0) {
                    visited[next] = 1;
                    que.add(next);
                }
            }
        }   
    }
}