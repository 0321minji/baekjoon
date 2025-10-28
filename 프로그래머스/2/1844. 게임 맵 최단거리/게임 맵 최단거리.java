import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        answer=bfs(maps);
        return answer;
    }
    
    private int bfs(int[][] maps){
        
        int[] dx=new int[]{0,0,1,-1};
        int[] dy=new int[]{1,-1,0,0};
        int n= maps.length;
        int m = maps[0].length;
        int[][] visited = new int[n][m];
        visited[0][0]=1;
        
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0,0,1});
        
        while (!q.isEmpty()){
            int[] now = q.poll();
            int x=now[0];
            int y=now[1];
            int cnt=now[2];
            
            if(x==n-1&&y==m-1){
                return cnt;
            }
            
            for(int i=0;i<4;i++){
                int nx=x+dx[i];
                int ny=y+dy[i];
                
                if ((0<=nx&&nx<n)&&(0<=ny&&ny<m)&&(visited[nx][ny]==0)&&maps[nx][ny]==1){
                    visited[nx][ny]=1;
                    q.add(new int[]{nx,ny,cnt+1});
                }
            }
        }
        return -1;
        
        
    }
}