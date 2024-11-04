
import java.util.*;

public class Main {
    static List<List<Integer>> graph;
    static boolean[] visit;

    public static void dfs(int i){
        System.out.print(i+" ");
        for (int nxt : graph.get(i)){
            if(!visit[nxt]){
                visit[nxt]=true;
                dfs(nxt);
            }
        }
    }

    public static void bfs(int i){
        Queue<Integer> que = new LinkedList<>();
        que.add(i);
        while (!que.isEmpty()){
            int now = que.poll();
            System.out.print(now+" ");
            for (int nxt :graph.get(now)){
                if (!visit[nxt]){
                    visit[nxt]=true;
                    que.add(nxt);
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int v = sc.nextInt();

        //graph 생성
        graph = new ArrayList<>(n+1);
        for (int i=0;i<=n;i++){
            graph.add(new ArrayList<>());
        }

        //초기값
        for (int i =0; i <m; i++){
            int a= sc.nextInt();
            int b= sc.nextInt();
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        for (int i=1;i<=n;i++){
            Collections.sort(graph.get(i));
        }

        visit = new boolean[n+1];
        visit[v]=true;
        dfs(v);
        System.out.println();
        Arrays.fill(visit,false);
        visit[v]=true;
        bfs(v);
        sc.close();
    }
}
