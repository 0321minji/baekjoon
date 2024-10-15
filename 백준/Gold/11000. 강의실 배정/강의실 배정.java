import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=Integer.parseInt(sc.nextLine());

        int [][] time = new int[n][2];
        for (int i=0; i<n; i++){
            time[i][0]=sc.nextInt();
            time[i][1]=sc.nextInt();
        }
        Arrays.sort(time,(a,b)->a[0]-b[0]);
        PriorityQueue<Integer> result = new PriorityQueue<>();
        result.offer(time[0][1]);

        for(int i=1; i<n;i++){
            if(result.peek()<=time[i][0]){
                result.poll();
            }
            result.offer(time[i][1]);
        }
        System.out.println(result.size());
        sc.close();
    }
}
