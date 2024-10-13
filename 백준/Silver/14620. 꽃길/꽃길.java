import java.util.*;
public class Main {
    // 변수 선언
    static int n;
    static int[][] flower;
    static int[][] move =  {{0,1},{0,-1},{1,0},{-1,0},{0,0}};
    static int result = 3000;

    // 심을 수 있는지 체크하는 함수
    // cf) for문에서 배열 활용(https://pathas.tistory.com/126)
    // cf) list array 비교 .. 자료구조 다 까먹음이슈.. (https://velog.io/@seongwon97/Java-Array%EC%99%80-List-%EB%B9%84%EA%B5%90)
    static boolean check(List<int[]> visit, int i, int j){
        for (int[] m:move){
            int[] nxt={i+m[0],j+m[1]};
            // if (visit.contains(nxt)){
            //     return false;
            // }
            //여기서 contains를 써서 비교하면 안되는 이유 : contains는 기본적으로 참조(주소값)비교        }
            if (containsArray(visit,nxt)){
                return false;
            }
        }
        return true;
    }
    static boolean containsArray(List<int[]> visit, int[] nxt){
        for (int[] v:visit){
            if (v[0]==nxt[0] && v[1]==nxt[1]){
                return true;
            }
        }
        return false;
    }

    static void solve(List<int[]> visit, int temp){
        if (result<=temp){
            return;
        } 
        if (visit.size()==15){
            result=Math.min(result,temp);
            return;
        }
        // 맨 바깥족 자리는 어차피 못심음
        for(int i=1;i<n-1;i++){
            for(int j=1;j<n-1;j++){
                if (check(visit,i,j)){
                    List<int[]> t=new ArrayList<>(visit);
                    int t_c=0;
                    for (int[] m:move){
                        int ni=i+m[0];
                        int nj=j+m[1];
                        t.add(new int[]{ni,nj});
                        t_c+=flower[ni][nj];
                    }
                    solve(t, temp+t_c);
                }
            }
        }
    }

    // 메인 함수
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        flower=new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                flower[i][j]=sc.nextInt();
            }
        }

        solve(new ArrayList<>(), 0);
        System.out.println(result);
        sc.close();
    }
}
