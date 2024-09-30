import java.util.*;

public class Main{
    public static void main(String[] args){
        //입력을 받기 위한 Scanner 객체 생성
        Scanner sc=new Scanner(System.in);
        // tc 수
        int t=sc.nextInt();
        // tc만큼 반복
        for(int i=0;i<t;i++){
            // 1. n,m 받아오기
            int n=sc.nextInt();
            int m=sc.nextInt();
            // 2. 중요도 받아오기

            List<Integer> important=new ArrayList<>();
            Queue<int[]> queue=new LinkedList<>();
            // 3. 중요도 받아와서 초기 위치와 함께 저장
            for (int j=0; j<n; j++){
                int priority=sc.nextInt();
                important.add(priority);
                queue.offer(new int[]{priority,j});
            }
            int cnt=0;
            // 최대 중요도 찾기
            while (true){
                int maxp=Collections.max(important);
                int[] current=queue.poll(); // 큐에서 문서 꺼냄

                if (current[0]==maxp){
                    cnt++;
                    if (current[1]==m){
                        System.out.println(cnt);
                        break;
                    }
                important.remove(Integer.valueOf(current[0]));
                }
                else{
                    queue.offer(current);
                }
            }
        }
        sc.close();
    }
}