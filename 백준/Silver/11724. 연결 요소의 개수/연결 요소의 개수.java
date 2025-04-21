import java.io.*;
import java.util.*;

public class Main {
    static int n,m;
    static boolean[][] graph;
    static boolean[] visited;
    static int count = 0;

    public static void dfs(int now){
        visited[now]=true;
        for(int i = 1; i <= n; i++) {
            if (graph[now][i] && !visited[i]) {
                dfs(i);
            }
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n= Integer.parseInt(st.nextToken());
        m= Integer.parseInt(st.nextToken());
        graph = new boolean[n+1][n+1];
        visited = new boolean[n+1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = true;
            graph[b][a] = true;
        }

        for(int i=1; i <= n; i++){
            if(!visited[i]){
                dfs(i);
                count++;
            }
        }

        System.out.println(count);
    }
}
