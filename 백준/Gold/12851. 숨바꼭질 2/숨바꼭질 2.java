import java.io.*;
import java.util.*;

public class Main {
    static int n,k;
    static int visited[];
    
    public static void bfs(){
        int time = 100001;
        int cnt = 0;


        Queue<int[]> que = new LinkedList<>();
        que.add(new int[]{n, 0});

        while (!que.isEmpty()){
            int[] current = que.poll();
            int now = current[0];
            int t = current[1];
            if (now==k){
                if (t<time){
                    time=t;
                    cnt=1;
                } else {
                    cnt+=1;
                }
            }
            int[] moves = {now+1, now-1, now*2};

            for (int nxt : moves){
                if (0<= nxt && nxt <100001){
                    if(visited[nxt]>= t+1) {
                        visited[nxt]=t+1;
                        que.add(new int[]{nxt, t+1});
                    }
                }
            }
        }
        System.out.println(time);
        System.out.println(cnt);
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n=Integer.parseInt(st.nextToken());
        k=Integer.parseInt(st.nextToken());

        visited = new int[100001];
        Arrays.fill(visited,100001);
        visited[n]=0;
        bfs();

    }
    
}
