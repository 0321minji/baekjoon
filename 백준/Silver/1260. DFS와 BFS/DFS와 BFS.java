import java.io.*;
import java.util.*;


public class Main {
    static int n,m,v;
    static boolean[][] graph;

    public static void dfs(int now, boolean[] visited){
        visited[now] = true;
        System.out.print(now + " ");
        for (int i = 1; i <= n; i++) {
            if (graph[now][i] && !visited[i]) {
                dfs(i, visited);
            }
        }
    }

    public static void bfs(int now, boolean[] visited){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(now);
        visited[now] = true;
        System.out.print(now + " ");
        
        while (!queue.isEmpty()) {
            int current = queue.poll();
            for (int i = 1; i <= n; i++) {
                if (graph[current][i] && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                    System.out.print(i + " ");
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());
        
        graph = new boolean[n+1][n+1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = true;
            graph[b][a] = true;
        }
        
        dfs(v, new boolean[n+1]);
        System.out.println();
        bfs(v, new boolean[n+1]);
    }
}